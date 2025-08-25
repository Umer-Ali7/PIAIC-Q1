# ⚡ n8n Workflow – Class 01 Automation  

This workflow was created in **Class 01 (PIAIC Q1 – Modern AI with Python & Agentic AI)**.  
It automates sending a welcome email to new students using **n8n + Gmail integration**.  

---

## 📌 Workflow Overview  

1. **Schedule Trigger** ⏰  
   - Starts the workflow at a defined interval (you can configure daily, hourly, etc.).  

2. **Edit Fields (Set Node)** ✍️  
   - Adds dynamic fields like `Name` and `Email`.  
   - Example:  
     ```json
     {
       "Name": "Umer Ali",
       "Email": "umerali54544@gmail.com"
     }
     ```

3. **Send a Message (Gmail Node)** 📧  
   - Sends an automated email with the subject:  
     *"Welcome to the Agentic AI & Robotics Course!"*  
   - Message:  
     ```
     Hello {{ $json.Name }}  
     You are a part of our Agentic AI & Robotics Course Program.  
     ```  

---

## 🚀 How to Use  

1. Import this workflow JSON into **n8n**.  
2. Connect your **Gmail credentials** in the Gmail node.  
3. Update the `Name` and `Email` fields (or connect to Google Sheets / DB for bulk).  
4. Activate the workflow and watch automated emails go out 🎉.  

---

## 📂 Repository Structure  

- **Onsite Classes** → Class-wise Python code.  
- **Assignments** → Homework and practice tasks.  
- **Workflows** → n8n workflow files (this file belongs here).  

👉 [View All Class Assignments Code Here](../onsite-classes)  
👉 [View All n8n Workflows Here](../onsite-n8n)  

---

## 📅 Created  
**Date:** August 17, 2025  
**Class:** PIAIC Q1 – Class 01  
**Instructors:** Mr. Aneeq & Mr. Hamza  
