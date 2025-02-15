# CLARINDA CAPSTONE - BIOTECHNOLOGY, BIOINFORMATICS, AND DATA SCIENCE
# CRUD Program Project
# Capstone 1

# Simulated user to access the DATABASE with roles and passwords
USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "researcher": {"password": "res123", "role": "Researcher"},
}

# Static Gene Database (10 Genetic Diseases)
DATABASE = {
    "1": {"GeneName": "BRCA1", "Description": "Tumor suppressor gene", "Function": "DNA repair",
           "Diseases": ["Breast cancer", "Ovarian cancer"], "Location": "Chromosome 17",
           "Mutations": "BRCA1 mutation", "Expression": "High",
           "MutationEffect": "Mutations impair DNA repair, increasing cancer risk."},
    "2": {"GeneName": "TP53", "Description": "Tumor suppressor gene", "Function": "Cell cycle regulation",
           "Diseases": ["Lung cancer", "Colon cancer"], "Location": "Chromosome 17",
           "Mutations": "TP53 mutation", "Expression": "Medium",
           "MutationEffect": "Disrupts cell cycle control and apoptosis, leading to tumors."},
    "3": {"GeneName": "CFTR", "Description": "Ion channel regulator", "Function": "Chloride ion transport",
           "Diseases": ["Cystic fibrosis"], "Location": "Chromosome 7",
           "Mutations": "CFTR mutation", "Expression": "Low",
           "MutationEffect": "Causes malfunctioning chloride channels, leading to thick mucus."},
    "4": {"GeneName": "MYC", "Description": "Oncogene", "Function": "Cell growth regulation",
           "Diseases": ["Leukemia", "Lymphoma"], "Location": "Chromosome 8",
           "Mutations": "MYC mutation", "Expression": "High",
           "MutationEffect": "Leads to uncontrolled cell proliferation and cancer development."},
    "5": {"GeneName": "EGFR", "Description": "Receptor tyrosine kinase", "Function": "Cell signaling and proliferation",
           "Diseases": ["Lung cancer", "Glioblastoma"], "Location": "Chromosome 7",
           "Mutations": "EGFR mutation", "Expression": "Medium",
           "MutationEffect": "Abnormal signaling promotes uncontrolled cell division."},
    "6": {"GeneName": "KRAS", "Description": "Oncogene", "Function": "Signal transduction",
           "Diseases": ["Pancreatic cancer", "Colon cancer"], "Location": "Chromosome 12",
           "Mutations": "KRAS mutation", "Expression": "High",
           "MutationEffect": "Causes constant activation of pathways driving cancer progression."},
    "7": {"GeneName": "HER2", "Description": "Growth factor receptor", "Function": "Cell proliferation",
           "Diseases": ["Breast cancer"], "Location": "Chromosome 17",
           "Mutations": "HER2 mutation", "Expression": "High",
           "MutationEffect": "Overexpression leads to aggressive breast cancer development."},
    "8": {"GeneName": "HBB", "Description": "Hemoglobin subunit beta", "Function": "Oxygen transport in red blood cells",
           "Diseases": ["Sickle cell disease", "Beta-thalassemia"], "Location": "Chromosome 11",
           "Mutations": "HBB mutation", "Expression": "Variable",
           "MutationEffect": "Alters hemoglobin structure, leading to anemia and organ damage."},
    "9": {"GeneName": "FBN1", "Description": "Fibrillin-1", "Function": "Formation of elastic fibers in connective tissue",
           "Diseases": ["Marfan syndrome"], "Location": "Chromosome 15",
           "Mutations": "FBN1 mutation", "Expression": "Medium",
           "MutationEffect": "Disrupts connective tissue formation, leading to cardiovascular issues."},
    "10": {"GeneName": "HTT", "Description": "Huntingtin protein", "Function": "Neuronal function and development",
           "Diseases": ["Huntington's disease"], "Location": "Chromosome 4",
           "Mutations": "Expanded CAG repeats in HTT", "Expression": "High (in brain)",
           "MutationEffect": "Abnormal protein with expanded polyglutamine tracts causes neurodegeneration."}
}

# ------------------------ 
# Datas

# -------------------------
# Function: Saving the DELETED_DATA to a different place and deleted gene entries 
# Purpose: For potential restoration
# -------------------------
DELETED_DATA = {}

#--------------------------
# Displaying the Database
#-------------------------

def display_database():
    """Displays all entries in the gene database."""
    print("\t".join(["Gene ID", "Gene Name", "Description", "Function", "Diseases", "Location", "Mutations", "Expression", "Mutation Effect"]))
    for gene_id, details in DATABASE.items():
        print("\t".join([
            gene_id, details["GeneName"], details["Description"], details["Function"],
            ", ".join(details["Diseases"]), details["Location"], details["Mutations"],
            details["Expression"], details["MutationEffect"]
        ]))
# -------------------------
# Function: display_menu
# Purpose: Displays the main menu options to the user.
# -------------------------

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Genetic Disease Database ---")
    print("1. View All Gene Entries")
    print("2. Add a Gene Entry (Admin/Researcher)")
    print("3. Update a Gene Entry (Admin/Researcher)")
    print("4. Delete a Gene Entry (Admin/Researcher)")
    print("5. Restore Deleted Data (Admin Only)")
    print("6. Log In")
    print("7. Logout")
    print("8. Exit")

# -------------------------
# Function: Authenticate or Verify
# Purpose: Authenticates or Verify a user based on role (ID) and password.
# -------------------------

def verify():
    """Authenticates the user based on role and password."""
    role_input = input("Role (admin, researcher): ").strip().lower()
    password = input("Password: ").strip()
    user = USERS.get(role_input)
    if user and user["password"] == password:
        print(f"\nLogin successful! Welcome, {role_input.capitalize()}.\n")
        return user["role"]
    else:
        print("Invalid role or password. Please try again.\n")
        return None
    
# -------------------------
# Function: confirm_action
# Purpose: Asks the user for confirmation before proceeding.
# -------------------------

def confirm_action(message="Are you sure? (yes/no): "):
    """Asks the user for confirmation before proceeding with an action."""
    confirmation = input(message).strip().lower()
    return confirmation == "yes"

# -------------------------
# Function: list_gene_entries
# Purpose: Lists all the gene entries in the DATABASE.
# -------------------------

def list_gene_entries():
    """Lists all gene entries in the DATABASE."""
    print("\n--- Gene Entries ---")
    if not DATABASE:
        print("No gene entries found.")
        return
    for gene_id, details in DATABASE.items():
        print(f"\nGeneID: {gene_id}")
        print(f"  Gene Name: {details['GeneName']}")
        print(f"  Description: {details['Description']}")
        print(f"  Function: {details['Function']}")
        print(f"  Diseases: {', '.join(details['Diseases'])}")
        print(f"  Location: {details['Location']}")
        print(f"  Mutations: {details['Mutations']}")
        print(f"  Expression: {details['Expression']}")
        print(f"  Mutation Effect: {details['MutationEffect']}")

# -------------------------
# Function: add_gene_entry
# Purpose: Adds a new gene entry to the DATABASE.
# -------------------------

def add_gene_entry():
    """Adds a new gene entry to the DATABASE with an automatically generated Gene ID."""
    next_id = str(len(DATABASE) + 1)  # Automatically generate the next Gene ID
    gene_name = input("Gene Name: ").strip()
    description = input("Description: ").strip()
    function = input("Function: ").strip()
    diseases = input("Diseases (separate with commas): ").strip().split(",")
    location = input("Location: ").strip()
    mutations = input("Known Mutations: ").strip()
    expression = input("Expression Level: ").strip()
    mutation_effect = input("Effect of Mutation: ").strip()

# -------------------------
# Function: confirm_action
# Purpose: Asks the user for confirmation before proceeding.
# -------------------------

    if confirm_action("Are you sure you want to add this gene entry? (yes/no): "):
        DATABASE[next_id] = {
            "GeneName": gene_name,
            "Description": description,
            "Function": function,
            "Diseases": [d.strip() for d in diseases if d.strip()],
            "Location": location,
            "Mutations": mutations,
            "Expression": expression,
            "MutationEffect": mutation_effect
        }
        print("Gene entry added successfully!")

# -------------------------
# Function: update_gene_entry
# Purpose: Updates an existing gene entry in the DATABASE.
# -------------------------

def update_gene_entry():
    """Updates an existing gene entry in the DATABASE."""
    gene_id = input("Enter GeneID to update: ").strip()
    if gene_id not in DATABASE:
        print("Error: GeneID not found.")
        return
    gene = DATABASE[gene_id]

    gene["GeneName"] = input(f"Gene Name ({gene['GeneName']}): ").strip() or gene["GeneName"]
    gene["Description"] = input(f"Description ({gene['Description']}): ").strip() or gene["Description"]
    gene["Function"] = input(f"Function ({gene['Function']}): ").strip() or gene["Function"]
    diseases = input(f"Diseases ({', '.join(gene['Diseases'])}): ").strip()
    if diseases:
        gene["Diseases"] = [d.strip() for d in diseases.split(",") if d.strip()]
    gene["Location"] = input(f"Location ({gene['Location']}): ").strip() or gene["Location"]
    gene["Mutations"] = input(f"Known Mutations ({gene['Mutations']}): ").strip() or gene["Mutations"]
    gene["Expression"] = input(f"Expression ({gene['Expression']}): ").strip() or gene["Expression"]
    gene["MutationEffect"] = input(f"Mutation Effect ({gene['MutationEffect']}): ").strip() or gene["MutationEffect"]

    if confirm_action("Are you sure you want to update this gene entry? (yes/no): "):
        print("Gene entry updated successfully!")

# -------------------------
# Function: delete_gene_entry
# Purpose: Deletes a gene entry from the DATABASE and moves it to DELETED_DATA.
# -------------------------

def delete_gene_entry():
    """Deletes a gene entry from the DATABASE and moves it to DELETED_DATA."""
    gene_id = input("Enter GeneID to delete: ").strip()
    if gene_id in DATABASE:
        if confirm_action("Are you sure you want to delete this gene entry? (yes/no): "):
            DELETED_DATA[gene_id] = DATABASE.pop(gene_id)
            print(f"Gene entry {gene_id} deleted successfully!")
    else:
        print("Error: GeneID not found.")

# -------------------------
# Function: restore_deleted_entry
# Purpose: Restores a deleted gene entry from DELETED_DATA back to DATABASE (Admin only).
# -------------------------

def restore_deleted_entry():
    """Restores a deleted gene entry from DELETED_DATA back to DATABASE (Admin only)."""
    if not DELETED_DATA:
        print("No deleted entries available to restore.")
        return
    print("\n--- Deleted Gene Entries ---")
    for gene_id, details in DELETED_DATA.items():
        print(f"\nGeneID: {gene_id}")
        print(f"  Gene Name: {details['GeneName']}")
        print(f"  Description: {details['Description']}")
        print(f"  Function: {details['Function']}")
        print(f"  Diseases: {', '.join(details['Diseases'])}")
        print(f"  Location: {details['Location']}")
        print(f"  Mutations: {details['Mutations']}")
        print(f"  Expression: {details['Expression']}")
        print(f"  Mutation Effect: {details['MutationEffect']}")
    
    gene_id = input("\nEnter GeneID to restore: ").strip()
    if gene_id in DELETED_DATA:
        if confirm_action("Are you sure you want to restore this deleted gene entry? (yes/no): "):
            DATABASE[gene_id] = DELETED_DATA.pop(gene_id)
            print(f"Gene entry {gene_id} restored successfully!")
    else:
        print("Error: GeneID not found in deleted entries.")

# -------------------------
# Main Function: The entry point for the program.
# -------------------------

def main():
    """Main function: The entry point for the program."""
    role = None  # No user is logged in initially.
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            list_gene_entries()
        elif choice == "2":
            if role in ["Admin", "Researcher"]:
                add_gene_entry()
            else:
                print("Permission denied. Please log in as Admin or Researcher.")
        elif choice == "3":
            if role in ["Admin", "Researcher"]:
                update_gene_entry()
            else:
                print("Permission denied. Please log in as Admin or Researcher.")
        elif choice == "4":
            if role in ["Admin", "Researcher"]:
                delete_gene_entry()
            else:
                print("Permission denied. Please log in as Admin or Researcher.")
        elif choice == "5":
            if role == "Admin":
                restore_deleted_entry()
            else:
                print("Permission denied. You need to log in as Admin to restore deleted entries.")
        elif choice == "6":
            role = verify()
        elif choice == "7":
            print("Logging out...")
            role = None
        elif choice == "8":
            print("Exiting Program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function when the script is executed.
if __name__ == "__main__":
    main()