/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.hoangthuan.mathutil.core;

/**
 *
 * @author Nguyen Hoang Thuan
 */
public class MathUtil {

    // Hàm tính giai thừa, n! = 1 * 2 * ... * n
    // 0! = 1 và 1! = 1
    // 21! sẽ bị tràn kiểu long vì có 18 số 0
    // Không tính được âm giai thừa
    
    //region - Hàm tính giai thừa (hàm mới)
    public static long getFactorial (int n) {
        
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

        if (n < 0 || n > 20)
            throw new IllegalArgumentException("n must be between 0..20");
        
        if (n == 0 || n == 1)
            return 1;   // Điểm dừng của đệ quy
        
        return n * getFactorial(n - 1);
    }
    //endregion
    
    //region - Hàm tính giai thừa (hàm cũ)
//    public static long getFactorial (int n) {
//        // Test-driven development
//        
//        if (n < 0 || n > 20)
//            throw new IllegalArgumentException("n must be between 0..20");
//        
//        if (n == 0 || n == 1)
//            return 1;
//        
//        // Phép nhân, khởi đầu giai thừa = 1
//        long product = 1;
//        
//        for (int i = 2; i <= n; i++) {
//            product *= i;
//        }
//        return product;
//    }
    //endregion
}
