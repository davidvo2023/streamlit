import streamlit as st
import requests
import ssl
import socket
import whois  # For fetching WHOIS information
import matplotlib.pyplot as plt

# Function to check WHOIS information
def get_whois_info(url, progress):
    try:
        domain = whois.whois(url)
        progress.progress(33)  # Update progress to 33% after WHOIS lookup
        st.write("WHOIS lookup successful...")  # Console log equivalent
        return domain
    except Exception as e:
        progress.progress(100)  # Complete progress in case of an error
        st.write("Error during WHOIS lookup!")  # Console log equivalent
        return None

# Function to check SSL certificate validity
def check_ssl_certificate(url, progress):
    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
        conn.settimeout(3)
        conn.connect((hostname, 443))  # Connect to the website on port 443
        cert = conn.getpeercert()
        progress.progress(66)  # Update progress to 66% after SSL check
        st.write("SSL certificate is valid!")  # Console log equivalent
        return cert
    except Exception as e:
        progress.progress(100)  # Complete progress in case of an error
        st.write("SSL certificate is invalid or couldn't be verified!")  # Console log equivalent
        return None

# Function to check HTTP headers for security
def check_http_headers(url, progress):
    try:
        response = requests.get(url)
        headers = response.headers
        # Security headers to look for
        security_headers = {
            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
            "Content-Security-Policy": headers.get("Content-Security-Policy"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
            "X-Frame-Options": headers.get("X-Frame-Options"),
            "X-XSS-Protection": headers.get("X-XSS-Protection"),
            "Referrer-Policy": headers.get("Referrer-Policy"),
        }
        progress.progress(100)  # Complete progress after checking headers
        st.write("HTTP Security Headers check completed.")  # Console log equivalent
        return security_headers
    except requests.exceptions.RequestException as e:
        progress.progress(100)  # Complete progress in case of an error
        st.write("Error while fetching HTTP headers!")  # Console log equivalent
        return None

# Streamlit interface
st.title("Website Security & WHOIS Check")

# Layout for URL input and button
 
with st.container():
    url = st.text_input("Enter the website URL for analysis:", "")

with st.container():
    check_button = st.button("Check")

# Hiển thị kết quả
if check_button:
    st.write(f"URL: {url}")

# Run analysis when the button is clicked
if check_button and url:
    # Create a progress bar
    progress = st.progress(0)  # Initialize progress bar at 0%

    # Get WHOIS Information
    st.header("WHOIS Information")
    whois_info = get_whois_info(url, progress)
    if whois_info:
        st.write("**WHOIS Information for Domain**:")
        st.write(f"**Domain Name**: {whois_info.get('domain_name')}")
        st.write(f"**Registrar**: {whois_info.get('registrar')}")
        st.write(f"**Creation Date**: {whois_info.get('creation_date')}")
        st.write(f"**Expiration Date**: {whois_info.get('expiration_date')}")
        st.write(f"**Country**: {whois_info.get('country')}")
    else:
        st.write("Could not fetch WHOIS information for this domain.")

    # Check SSL certificate
    st.header("SSL/TLS Certificate Check")
    ssl_cert = check_ssl_certificate(url, progress)
    if ssl_cert:
        st.write("The website has a valid SSL/TLS certificate!")
        st.write(f"Certificate details: {ssl_cert}")
    else:
        st.write("The website does not have a valid SSL/TLS certificate or could not be verified.")

    # Check HTTP Security Headers
    st.header("HTTP Security Headers Check")
    headers = check_http_headers(url, progress)
    if headers:
        st.write("Security headers found:")
        for header, value in headers.items():
            if value:
                st.write(f"**{header}:** {value}")
            else:
                st.write(f"**{header}:** Not present")
    else:
        st.write("Could not retrieve HTTP headers or make a request to the website.")

    # Additional Security Check: Ensure HTTPS
    if url.startswith("https://"):
        st.write("The website is using HTTPS (secure connection).")
    else:
        st.write("The website is not using HTTPS. Consider using HTTPS for secure communication.")

    # Generate a pie chart to visualize the security evaluation
    st.header("Website Security Evaluation")

    # Evaluate the security based on results (arbitrary scoring system)
    score = 0
    total_checks = 3  # WHOIS, SSL, HTTP Headers
    
    # WHOIS Check
    if whois_info:
        score += 1
    
    # SSL Certificate Check
    if ssl_cert:
        score += 1
    
    # HTTP Headers Check
    if headers and all(headers.values()):
        score += 1
    
    # Pie chart with scores
    labels = ['Secure', 'Needs Improvement']
    sizes = [score, total_checks - score]
    colors = ['#66b3ff', '#ff6666']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.pyplot(fig)  # Show the pie chart
