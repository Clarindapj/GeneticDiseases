# **Capstone Project 1:**
# **System for Managing Databases of Genetic Disorders**

# 1. Background

- The Genetic Diseases Database Management System is a program which encapsulates my Capstone Project at **PURWADHIKA Data Science Program JCDS-206.** It is designed to operate within the construct of a CRUD application.

- My primary focus has always been on `Biology, Biotechnology, and Bioinformatics.` I find particular interest in how genetic information can be harnessed in `medical research.`
- To advance this knowledge, I am currently learning about `data science`, which `applies computer science methods to biological research.`
- This project is a great step towards integrating these areas and allows me to apply data science principles into research of genetic diseases.

- This project was quite challenging, but it was also worthwhile. Although my background is in Biotechnology and Bioinformatics, as I worked on this project, I found myself learning to think critically about the problems at hand and to think logically and computationally in ways that I did not think were possible before.
  
- This project has significantly enhanced my programming skills, but most importantly, it has transformed my perspective on data science as a discipline and its significance to the field of genetics. I am eagerly anticipating further and continuous advancement due to the ability to undertake such tasks.
  
# 2. Objectives:

This project primarily aims to establish a role-based CRUD (Create, Read, Update, and Delete) genetic disease database system. The system is able to:

- Allow the structured storage of genetic disease information.

- Provide role-based access.

- Retrieve and change gene information efficiently.

- Restore deleted records to maintain integrity of data.

# 3. Project Scope:

- Design and develop a system for management of genetics diseases associated with Python.

- Develop a simulation of a static database.

- Implement role-based access for Admins and Researchers.

- Implement genetic data management CRUD functionalities.

- Have the ability to restore deleted data entries for integrity reasons.

# 4. System Features

## Role-Based Authentication

The system is stratified into two categories:

- **Admin**: Full access includes the ability to add, edit, remove, and restore old entries.

- **Researcher**: Users that can add, edit and delete data but cannot restore any deleted data.

## Public Access

- Everyone who is *logged in* or not at all have the option of *searching* the database associated with genetic disorders.

- Only **Admins** and **Researchers** who are logged in may edit, delete, or restore the records of the system.

## Data Structure

The System is storing genetic data in form of a Python structure; each entry should contain:

  - **Gene Name**: The designation of the gene.

  - **Description**: A brief detail of the gene.

  - **Function**: The role in metabolism of the gene.

  - **Diseases**: List of some diseases caused by the mutations in the gene.

  - **Location**: The locus of the gene on the chromosome.

  - **Mutations**: Some common changes which occur in the gene.

  - **Expression**: Levels of expression of the gene.

  - **Mutation Effect**: The effect of the mutations in the gene on living organisms.


# 5. CRUD Operations Program 

The system does work with the following features:

  - **Access Gene Data:** Allows users to view all gene entries in an organized manner irrespective of their roles.

  - **Add Gene Entry:** A function that allows Admins and Researchers to put new gene entries in the system.

  - **Update Gene Entry:** Allows authorized users to amend the particulars of a specific gene.

  - **Remove Gene Entry:** An action that deletes a gene from the system with the ability to retrieve it if needed.

  - **Restore Deleted Entry:** Admins retrieve or restore the deleted gene records.

## Main Menu Functions
Once the program starts, the user has the following options on the menu:

  - **View All Gene Entries:** Present all noted gene entries (available to all users).

  - **Add a Gene Entry:** Add further new gene details (Admin/Researcher).

  - **Update a Gene Entry:** Change previously added data (Admin/Researcher).

  - **Delete a Gene Entry:** Deletion moves a backup copy to store and access later (Admin/Researcher).

  - **Restore Deleted Data:** Retrieve deleted gene entries (Admin Only).

  - **Log In:** Users authenticate themselves to access the system based on their roles.

  - **Log Out:** The current user is logged out.

  - **Exit:** The program is turned off.

# 6. Implementation Details

## Libraries Used

- *Python Standard Libraries*: The project did not require any additional third party libraries as it was developed using built in Python modules.

## Program Flow

1. Users are able to *view* data of genetic disease records before they log in to the system.

2. Users may log in as either *Admin* or *Researcher* and have modification capabilities enabled.

3. The users are able to utilize some features that are specific to the role they have selected from the main menu.

4. The system uses a dictionary to store gene data.

5. Deleted information is kept for archival reasons in case it needs to be restored.

6. Users have the option of logging out or quitting the program whenever they see fit.

# 7. Testing and Validation

The following will be tested:

- Check whether all CRUD functions are executed and processed in the system correctly.

- Ensure authorizations based on defined user roles are enforced.

- Examine the system for possible data corruption from overwriting or deleting records entries.

- Validate that information is publicly accessible to allow viewing, but not unauthorized editing.

# 8. File Structure
- 📂 CAPSTONE1_Clarinda_Genetic_Diseases_Program.py – Main Python Script
- 📂 ReadMe_Capstone_Genetic_Disease_Clarinda.md – Detailed Project Background
- 📂 ReadMe_2_Genetic_Disease_Informations.md – Additional Genetic Data For Testing

# 9. Future Enhancements
- 🚀 Implement a GUI for user-friendly interaction
- 🚀 Expand the database with real-world genetic data sources
- 🚀 Integrate machine learning for mutation impact predictions

# 10. Conclusion

This project greatly increased my programming abilities, which would allow me to assume my role as a database manager as well as a biological researcher at a large-scale institution. This work for sure has driven my passion to apply Biotechnology, Bioinformatics, and Data Science integration to practical problems through my research works. I must admi# **Capstone Project 1:**
# **System for Managing Databases of Genetic Disorders**

# 1. Background

- The Genetic Diseases Database Management System is a program which encapsulates my Capstone Project at **PURWADHIKA Data Science Program JCDS-206.** It is designed to operate within the construct of a CRUD application.

- My primary focus has always been on `Biology, Biotechnology, and Bioinformatics.` I find particular interest in how genetic information can be harnessed in `medical research.`
- To advance this knowledge, I am currently learning about `data science`, which `applies computer science methods to biological research.`
- This project is a great step towards integrating these areas and allows me to apply data science principles into research of genetic diseases.

- This project was quite challenging, but it was also worthwhile. Although my background is in Biotechnology and Bioinformatics, as I worked on this project, I found myself learning to think critically about the problems at hand and to think logically and computationally in ways that I did not think were possible before.
  
- This project has significantly enhanced my programming skills, but most importantly, it has transformed my perspective on data science as a discipline and its significance to the field of genetics. I am eagerly anticipating further and continuous advancement due to the ability to undertake such tasks.
  
# 2. Objectives:

This project primarily aims to establish a role-based CRUD (Create, Read, Update, and Delete) genetic disease database system. The system is able to:

- Allow the structured storage of genetic disease information.

- Provide role-based access.

- Retrieve and change gene information efficiently.

- Restore deleted records to maintain integrity of data.

# 3. Project Scope:

- Design and develop a system for management of genetics diseases associated with Python.

- Develop a simulation of a static database.

- Implement role-based access for Admins and Researchers.

- Implement genetic data management CRUD functionalities.

- Have the ability to restore deleted data entries for integrity reasons.

# 4. System Features

## Role-Based Authentication

The system is stratified into two categories:

- **Admin**: Full access includes the ability to add, edit, remove, and restore old entries.

- **Researcher**: Users that can add, edit and delete data but cannot restore any deleted data.

## Public Access

- Everyone who is *logged in* or not at all have the option of *searching* the database associated with genetic disorders.

- Only **Admins** and **Researchers** who are logged in may edit, delete, or restore the records of the system.

## Data Structure

The System is storing genetic data in form of a Python structure; each entry should contain:

  - **Gene Name**: The designation of the gene.

  - **Description**: A brief detail of the gene.

  - **Function**: The role in metabolism of the gene.

  - **Diseases**: List of some diseases caused by the mutations in the gene.

  - **Location**: The locus of the gene on the chromosome.

  - **Mutations**: Some common changes which occur in the gene.

  - **Expression**: Levels of expression of the gene.

  - **Mutation Effect**: The effect of the mutations in the gene on living organisms.


# 5. CRUD Operations Program 

The system does work with the following features:

  - **Access Gene Data:** Allows users to view all gene entries in an organized manner irrespective of their roles.

  - **Add Gene Entry:** A function that allows Admins and Researchers to put new gene entries in the system.

  - **Update Gene Entry:** Allows authorized users to amend the particulars of a specific gene.

  - **Remove Gene Entry:** An action that deletes a gene from the system with the ability to retrieve it if needed.

  - **Restore Deleted Entry:** Admins retrieve or restore the deleted gene records.

## Main Menu Functions
Once the program starts, the user has the following options on the menu:

  - **View All Gene Entries:** Present all noted gene entries (available to all users).

  - **Add a Gene Entry:** Add further new gene details (Admin/Researcher).

  - **Update a Gene Entry:** Change previously added data (Admin/Researcher).

  - **Delete a Gene Entry:** Deletion moves a backup copy to store and access later (Admin/Researcher).

  - **Restore Deleted Data:** Retrieve deleted gene entries (Admin Only).

  - **Log In:** Users authenticate themselves to access the system based on their roles.

  - **Log Out:** The current user is logged out.

  - **Exit:** The program is turned off.

# 6. Implementation Details

## Libraries Used

- *Python Standard Libraries*: The project did not require any additional third party libraries as it was developed using built in Python modules.

## Program Flow

1. Users are able to *view* data of genetic disease records before they log in to the system.

2. Users may log in as either *Admin* or *Researcher* and have modification capabilities enabled.

3. The users are able to utilize some features that are specific to the role they have selected from the main menu.

4. The system uses a dictionary to store gene data.

5. Deleted information is kept for archival reasons in case it needs to be restored.

6. Users have the option of logging out or quitting the program whenever they see fit.

# 7. Testing and Validation

The following will be tested:

- Check whether all CRUD functions are executed and processed in the system correctly.

- Ensure authorizations based on defined user roles are enforced.

- Examine the system for possible data corruption from overwriting or deleting records entries.

- Validate that information is publicly accessible to allow viewing, but not unauthorized editing.

# 8. File Structure
- 📂 CAPSTONE1_Clarinda_Genetic_Diseases_Program.py – Main Python Script
- 📂 ReadMe_Capstone_Genetic_Disease_Clarinda.md – Detailed Project Background
- 📂 ReadMe_2_Genetic_Disease_Informations.md – Additional Genetic Data For Testing

# 9. Future Enhancements
- 🚀 Implement a GUI for user-friendly interaction
- 🚀 Expand the database with real-world genetic data sources
- 🚀 Integrate machine learning for mutation impact predictions

# 10. Conclusion

This project greatly increased my programming abilities, which would allow me to assume my role as a database manager as well as a biological researcher at a large-scale institution. This work for sure has driven my passion to apply Biotechnology, Bioinformatics, and Data Science integration to practical problems through my research works. I must admit that the knowledge I gathered exceeds the initial expectations set upon myself.


### With all regards,
**Clarinda Puspitajati.**
