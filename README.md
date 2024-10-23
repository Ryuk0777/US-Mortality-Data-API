# 🏥 **USA Mortality Data API**

A RESTful API to access and analyze **USA Mortality Data (2011–2013)**, categorized by region, gender, cause of death, and urban/rural status. Built with Python's **Flask** framework, the dataset is stored in **MongoDB** after processing from CSV format.

---

## 🌟 **Project Overview**

This API allows users to query **mortality rates** across various dimensions, offering efficient data access for further analysis and visualization. It is designed for scalability, using MongoDB for data storage.

---

## ✨ **Features**

1. **Mortality Data API:** Query mortality data across multiple dimensions.
2. **MongoDB Storage:** Efficient and scalable solution for data storage.
3. **Python Flask:** Lightweight and flexible framework for building APIs.

---

## 🛠️ **Technologies Used**

- **Flask (Python)**  
- **MongoDB**  
- **Jupyter Notebook**
- **Pandas** (for CSV data processing)


<div align="center">
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183914128-3fc88b4a-4ac1-40e6-9443-9a30182379b7.png" alt="Jupyter Notebook" title="Jupyter Notebook"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png" alt="Flask" title="Flask"/></code>
	<code><img width="50" src="https://github.com/marwin1991/profile-technology-icons/assets/76012086/24b02d77-2f28-43c7-b5d6-e15e3395851b" alt="Pandas" title="Pandas"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/182884177-d48a8579-2cd0-447a-b9a6-ffc7cb02560e.png" alt="mongoDB" title="mongoDB"/></code>
</div>

---

## 🚀 **Usage:**

**Request URL:** `http://127.0.0.1:5000/<-Your Data Request->`

### **Data Requests:**

- **Region**  
- **Urban/Rural**  
- **Gender**  
- **Cause**  
- **Region-Urban/Rural**  
- **Cause-Urban/Rural**  
- **Cause-Gender**  
- **Region-Rural-Gender**  
- **Region-Urban-Gender**  
- **Cause-Urban-Gender**  
- **Cause-Rural-Gender**

**Example:**  
`http://127.0.0.1:5000/Region`

---

### 🗺️ **Data Requests by Region:**

1. **HHS<-Region No->-Cause**  
   `Example:` `http://127.0.0.1:5000/HHS1-Cause`

2. **HHS<-Region No->-Urban/Rural**  
   `Example:` `http://127.0.0.1:5000/HHS1-Urban || Rural`

3. **HHS<-Region No->-Gender**  
   `Example:` `http://127.0.0.1:5000/HHS1-Gender`

4. **HHS<-Region No->-Cause-Urban/Rural**  
   `Example:` `http://127.0.0.1:5000/HHS1-Cause-Urban || Rural`

5. **HHS<-Region No->-Cause-Gender**  
   `Example:` `http://127.0.0.1:5000/HHS1-Cause-Gender`

6. **HHS<-Region No->-Urban/Rural-Cause**  
   `Example:` `http://127.0.0.1:5000/HHS1-Urban || Rural-Cause`

---
