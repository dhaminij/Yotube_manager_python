import requests

BASE_URL = "https://reqres.in/api/users"

def get_users():
    print("\n Getting users...")
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        for user in data['data']:
            print(f"{user['id']}: {user['first_name']} {user['last_name']} - {user['email']}")
    else:
        print(" Failed to retrieve users")

def create_user():
    print("\n Creating new user...")
    name = input("Enter name: ")
    job = input("Enter job: ")
    payload = {"name": name, "job": job}
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        data = response.json()
        print(" User created:", data)
    else:
        print(" Failed to create user")

def update_user():
    print("\n Updating user...")
    user_id = input("Enter user ID to update: ")
    name = input("Enter new name: ")
    job = input("Enter new job: ")
    payload = {"name": name, "job": job}
    response = requests.put(f"{BASE_URL}/{user_id}", json=payload)
    if response.status_code == 200:
        print(" User updated:", response.json())
    else:
        print(" Failed to update user")

def delete_user():
    print("\ Deleting user...")
    user_id = input("Enter user ID to delete: ")
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 204:
        print(" User deleted successfully.")
    else:
        print(" Failed to delete user.")

def main():
    while True:
        print("\n=== User Manager App ===")
        print("1. View Users (GET)")
        print("2. Create User (POST)")
        print("3. Update User (PUT)")
        print("4. Delete User (DELETE)")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            get_users()
        elif choice == '2':
            create_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print(" Exiting app. Bye!")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
