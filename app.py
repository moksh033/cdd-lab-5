# Application Server (CDD Lab 5)

def get_backend_status():
    return {"status": "healthy", "service": "cdd-api", "version": "1.0.0"}

def main():
    print("Welcome to CDD Lab 5 Team Collaboration Service")
    print("Status:", get_backend_status())

if __name__ == "__main__":
    main()
