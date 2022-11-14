package com.hoangthuan.mathutil.core;

/*
 * Class này cung cấp các tiện ích (utility),
 * một loạt các hàm toán học để hỗ trợ cho các class khác sử dụng,
 * tiện ích dùng chung nên được thiết kế là static
 * 
 * (Có hai kỹ thuật để viết hàm này.
 *  Vì vậy, rất thích hợp để minh hoạ cho kỹ thuật
 *  hồi quy (regression) và tối ưu (refactor) code
 */
public class MathUtil {
    
    // Test-driven development

    // Hàm tính giai thừa, n! = 1 * 2 * ... * n
    //
    // Quy ước:
    //          0! = 1 và 1! = 1
    //
    //          Không tính được giai thừa cho số âm
    //
    //          Vì giai thừa sẽ tăng rất nhanh về trọng số,
    //          mà kiểu dữ liệu long chỉ được phép có tối đa 18 số 0,
    //          nếu 21! thì sẽ bị tràn kiểu long vì có đến 19 số 0
    //          nên 20! là vừa đủ,
    
    //region - Hàm tính giai thừa (hàm mới),
    //         viết theo kiểu đệ quy
    public static long getFactorial(int n) {

        // Đệ quy (recursion): phương pháp gọi lại chính mình
        // với quy mô khác
        //
        // Ví dụ:
        //      5! = 1 * 2 * 3 * 4 * 5 = 120
        //
        //      5! = 5 * 4!
        //      4! = 4 * 3!
        //      3! = 3 * 2!
        //      2! = 2 * 1!
        //      1! = 1 -> Dừng
        //
        //      n! = n * (n - 1)! -> Công thức lặp lại chính mình
        if (n < 0 || n > 20) {
            throw new IllegalArgumentException("Invalid argument. "
                    + "n must be between 0..20");
        }

        if (n == 0 || n == 1) {
            return 1;   // Điểm dừng của đệ quy
        }
        return n * getFactorial(n - 1);
    }
    //endregion

    //region - Hàm tính giai thừa (hàm cũ),
    //         viết theo kiểu nhồi liên tục bằng for
//    public static long getFactorial (int n) {
//        
//        // Hàm sẽ văng ra ngoại lệ
//        // nếu đưa vào số âm hoặc số lớn hơn 20
//        if (n < 0 || n > 20)
//            // Hàm sẽ tự động dừng mà không cần return
//            throw new IllegalArgumentException("Invalid argument. "
//                    + "n must be between 0..20");
//
//        // Theo quy ước, 0! hay 1! đều là 1
//        if (n == 0 || n == 1)
//            // Lập tức dừng khi gặp trường hợp đặc biệt
//            return 1;
//    
//        // product: phép nhân (tích), kết quả trung gian,
//        // khởi đầu giai thừa = 1
//        long product = 1;
//    
//        // Nếu n < 0 || n > 20 || n == 0 || n == 1
//        // thì đã rơi vào những câu lệnh if ở trên,
//        // đến đây thì chắc chắn n = 2..20
//        for (int i = 2; i <= n; i++)
//            // Nhồi liên tục vào biến trung gian product
//            // với giá trị khởi tạo ban đầu = 1
//            product *= i;
//    
//        return product;
//    }
    //endregion
}
