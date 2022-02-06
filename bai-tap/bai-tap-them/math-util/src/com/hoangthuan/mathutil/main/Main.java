/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.hoangthuan.mathutil.main;

import com.hoangthuan.mathutil.core.MathUtil;

/**
 *
 * @author Nguyen Hoang Thuan
 */
public class Main {
    public static void main(String[] args) {
        
        // Test thủ công (Manual Testing)
        
        // Muốn thấy xuất hiện ngoại lệ hay không
        // thì cứ gọi để xem app bị giết
        //MathUtil.getFactorial(-5);
        
        System.out.println("0! | Mong đợi: 1 | Thực tế: "
                + MathUtil.getFactorial(0));
        
        System.out.println("1! | Mong đợi: 1 | Thực tế: "
                + MathUtil.getFactorial(1));
        
        System.out.println("2! | Mong đợi: 2 | Thực tế: "
                + MathUtil.getFactorial(2));
        
        System.out.println("5! | Mong đợi: 120 | Thực tế: "
                + MathUtil.getFactorial(5));
    }
    
}
