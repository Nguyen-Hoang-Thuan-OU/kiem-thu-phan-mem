/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.hoangthuan.mathutil.core;

import static com.hoangthuan.mathutil.core.MathUtil.getFactorial;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameter;
import org.junit.runners.Parameterized.Parameters;

/**
 *
 * @author Nguyen Hoang Thuan
 */

// Báo cho JUNit rằng class này là class tham số hoá
@RunWith(value = Parameterized.class)
public class AdvancedFactorialTest {
    
    // Tách toàn bộ dữ liệu cần test
    // gồm đầu vào và đầu ra sang một chỗ
    // (có thể là một file text, csv, excel, database,... riêng)
    // để dễ quản lý và đảm bảo đã bao đủ hết các trường hợp
    // (đây là được xem là Test Script tự động)
    
    // Tên hàm được đặt tự do
    // Khai báo tập hợp các tham số
    @Parameters
    public static Object[][] initData() {
        return new Integer[][] {
                                {0, 1},
                                {1, 1},
                                {2, 2},
                                {3, 6},
                                {4, 24},
                                {5, 120},
                                {6, 720}
                               };
    }
    
    // Chuẩn bị 2 biến để hứng bộ dữ liệu từ mảng
    // sau đó đưa vào hàm test
    
    // Ánh xạ input với cột 0
    @Parameter(value = 0)
    public int input;
    
    // Ánh xạ expected với cột 1
    @Parameter(value = 1)
    public long expected;
    
    // Nhận bộ dữ liệu kiểm thử và tự động tiến hành kiểm thử
    @Test
    public void checkFactorialGivenCorrectArgumentReturnWell() {

        assertEquals(expected, getFactorial(input));
    }
}