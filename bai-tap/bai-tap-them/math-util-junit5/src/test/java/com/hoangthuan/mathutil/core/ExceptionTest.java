package com.hoangthuan.mathutil.core;

import static com.hoangthuan.mathutil.core.MathUtil.getFactorial;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.function.Executable;

public class ExceptionTest {
    
    // Kiểm tra xem hàm có ném ra ngoại lệ
    // bằng một hàm static mới thuộc class Assertions
    
    // Đảm bảo tính nhất quán: ước lượng / đánh giá điều gì
    //                         có xảy ra hay không
    //      Ví dụ:
    //              assertTrue(): có trả về true hay không?
    //              assertEquals(): có trả về đúng giá trị hay không?
    //              assertThrows(): có ném ra gì hay không?
    //  -> Cùng một phong cách thiết kế
    
    // Sử dụng biểu thức lambda trong việc kiểm tra ngoại lệ bằng assertThrows()
    
    @Test
    public void checkFactorialGivenWrongArgumentThrowsException() {
        
        // Câu lệnh nào gây ra ngoại lệ
        // thì sẽ đưa nó vào biểu thức lambda
        
        // Trong JUnit 5 có một Functional Interface
        // tên là Executable ≈ Comparator
        // được sử dụng để chứa câu lệnh gây ra ngoại lệ
        // thông qua việc implements Interface này
        // (vì không được trực tiếp viết code trên Interface)
        
        // Viết theo phong cách truyền thống
//        Executable wrongArgument = new Executable() {
//            @Override
//            public void execute() throws Throwable {
//                MathUtil.getFactorial(-5);
//            }
//        }; // V.I.P
        // ≈ Executable wrongArgument = new Executable();
        
        // Viết theo phong cách biểu thức lambda
//        Executable wrongArgument = () -> {MathUtil.getFactorial(-5);};
        
        // Vì có có đúng một lệnh
//        Executable wrongArgument = () -> MathUtil.getFactorial(-5);
        
//        assertThrows(IllegalArgumentException.class, wrongArgument);

        // Vì tham số thứ hai chỉ cần nhận vào một Executable
        assertThrows(IllegalArgumentException.class,
                () -> MathUtil.getFactorial(-5));
    }
    
}
