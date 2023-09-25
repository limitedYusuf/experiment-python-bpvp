from datetime import datetime

class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

class LeaveRequest:
    def __init__(self, emp_id, start_date, end_date, reason):
        self.emp_id = emp_id
        self.start_date = start_date
        self.end_date = end_date
        self.reason = reason
        self.status = "Pending"

class LeaveRequestProcessor:
    def __init__(self):
        self.requests = []

    def submit_request(self, request):
        # Validasi tanggal
        start_date = datetime.strptime(request.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(request.end_date, "%Y-%m-%d")

        if start_date > end_date:
            print("Tanggal mulai harus sebelum tanggal berakhir.")
            return

        self.requests.append(request)

    def approve_request(self, request_id):
        for request in self.requests:
            if request.emp_id == request_id and request.status == "Pending":
                request.status = "Approved"
                print(f"Permintaan cuti oleh {request.emp_id} disetujui.")
                return

    def reject_request(self, request_id):
        for request in self.requests:
            if request.emp_id == request_id and request.status == "Pending":
                request.status = "Rejected"
                print(f"Permintaan cuti oleh {request.emp_id} ditolak.")
                return

    def list_requests(self):
        for request in self.requests:
            print(f"ID Pegawai: {request.emp_id}, Tanggal: {request.start_date} - {request.end_date}, Status: {request.status}")

def main():
    employees = [
        Employee("EMP001", "John Doe", "HR"),
        Employee("EMP002", "Jane Smith", "IT")
    ]

    leave_processor = LeaveRequestProcessor()

    leave_request1 = LeaveRequest("EMP001", "2023-10-01", "2023-10-05", "Liburan")
    leave_request2 = LeaveRequest("EMP002", "2023-11-15", "2023-11-20", "Keluarga")
    leave_processor.submit_request(leave_request1)
    leave_processor.submit_request(leave_request2)

    leave_processor.approve_request("EMP001")
    leave_processor.reject_request("EMP002")

    print("Daftar Permintaan Cuti:")
    leave_processor.list_requests()

if __name__ == "__main__":
    main()
