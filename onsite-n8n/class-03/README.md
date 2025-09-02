# 📘 Class 03 – Airtable Integration with n8n  

**Date:** Sunday, August 31, 2025  
**Instructors:** Sir Aneeq & Sir Hamza  
**Tool Used:** n8n + Airtable  

---

## 🎯 Objective  
In this class, we learned how to **connect n8n with Airtable** and automatically send data (like Name & Email) into an Airtable table.  

---

## ⚡ Workflow Overview  

The workflow has the following steps:  

1. **Manual Trigger**  
   - Starts the workflow when you click **Execute Workflow** in n8n.  

2. **Set Node (Edit Fields)**  
   - Used to define values for fields:  
     - `Name` → "Umer Ali"  
     - `Email` → "example@gmail.com"  

3. **Airtable Node (Create a Record)**  
   - Connects with Airtable using your **Personal Access Token**.  
   - Creates a new record in your selected **Base** and **Table**.  
   - Maps the fields:  
     - `Name` → value from Set Node  
     - `Email` → value from Set Node  

---

## 🛠️ How It Works  
- Jab bhi workflow run karte ho → n8n user ke **Name & Email** ko Airtable me ek nayi row ke taur par store kar deta hai.  
- Ye automation future me **form submissions**, **student records**, ya **contact lists** ke liye use ho sakta hai.  

---

## 🔮 Coming Next  
- Automating with **Google Sheets**.  
- Scheduling workflows with **n8n triggers**.  
- Using AI models (Gemini / OpenAI) inside workflows.  

---

✨ *This workflow helps us understand how to integrate external databases (like Airtable) with n8n to automate data entry.*  
