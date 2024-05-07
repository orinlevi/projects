	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 3
	.globl	_test                           ; -- Begin function test
	.p2align	2
_test:                                  ; @test
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	bl	_test_encode_non_cyclic_lower_case_positive_k
	cbz	w0, LBB0_2
	b	LBB0_1
LBB0_1:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_2:
	bl	_test_encode_cyclic_lower_case_special_char_positive_k
	cbz	w0, LBB0_4
	b	LBB0_3
LBB0_3:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_4:
	bl	_test_encode_non_cyclic_lower_case_special_char_negative_k
	cbz	w0, LBB0_6
	b	LBB0_5
LBB0_5:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_6:
	bl	_test_encode_cyclic_lower_case_negative_k
	cbz	w0, LBB0_8
	b	LBB0_7
LBB0_7:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_8:
	bl	_test_encode_cyclic_upper_case_positive_k
	cbz	w0, LBB0_10
	b	LBB0_9
LBB0_9:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_10:
	bl	_test_decode_non_cyclic_lower_case_positive_k
	cbz	w0, LBB0_12
	b	LBB0_11
LBB0_11:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_12:
	bl	_test_decode_cyclic_lower_case_special_char_positive_k
	cbz	w0, LBB0_14
	b	LBB0_13
LBB0_13:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_14:
	bl	_test_decode_non_cyclic_lower_case_special_char_negative_k
	cbz	w0, LBB0_16
	b	LBB0_15
LBB0_15:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_16:
	bl	_test_decode_cyclic_lower_case_negative_k
	cbz	w0, LBB0_18
	b	LBB0_17
LBB0_17:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_18:
	bl	_test_decode_cyclic_upper_case_positive_k
	cbz	w0, LBB0_20
	b	LBB0_19
LBB0_19:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB0_21
LBB0_20:
	stur	wzr, [x29, #-4]
	b	LBB0_21
LBB0_21:
	ldur	w0, [x29, #-4]
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_len                            ; -- Begin function len
	.p2align	2
_len:                                   ; @len
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32
	.cfi_def_cfa_offset 32
	str	x0, [sp, #16]
	str	wzr, [sp, #12]
	ldr	x8, [sp, #16]
	cbnz	x8, LBB1_2
	b	LBB1_1
LBB1_1:
	mov	w8, #1
	str	w8, [sp, #28]
	b	LBB1_8
LBB1_2:
	ldr	x8, [sp, #16]
	subs	x8, x8, #0
	b.ge	LBB1_4
	b	LBB1_3
LBB1_3:
	ldr	w8, [sp, #12]
	add	w8, w8, #1
	str	w8, [sp, #12]
	ldr	x9, [sp, #16]
	mov	x8, #0
	subs	x8, x8, x9
	str	x8, [sp, #16]
	b	LBB1_4
LBB1_4:
	b	LBB1_5
LBB1_5:                                 ; =>This Inner Loop Header: Depth=1
	ldr	x8, [sp, #16]
	subs	x8, x8, #0
	b.le	LBB1_7
	b	LBB1_6
LBB1_6:                                 ;   in Loop: Header=BB1_5 Depth=1
	ldr	x8, [sp, #16]
	mov	x9, #10
	sdiv	x8, x8, x9
	str	x8, [sp, #16]
	ldr	w8, [sp, #12]
	add	w8, w8, #1
	str	w8, [sp, #12]
	b	LBB1_5
LBB1_7:
	ldr	w8, [sp, #12]
	str	w8, [sp, #28]
	b	LBB1_8
LBB1_8:
	ldr	w0, [sp, #28]
	add	sp, sp, #32
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_test_of_args                   ; -- Begin function test_of_args
	.p2align	2
_test_of_args:                          ; @test_of_args
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #80
	stp	x29, x30, [sp, #64]             ; 16-byte Folded Spill
	add	x29, sp, #64
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	adrp	x8, ___stderrp@GOTPAGE
	ldr	x8, [x8, ___stderrp@GOTPAGEOFF]
	str	x8, [sp, #16]                   ; 8-byte Folded Spill
	stur	w0, [x29, #-8]
	stur	x1, [x29, #-16]
	ldur	w8, [x29, #-8]
	subs	w8, w8, #5
	b.eq	LBB2_3
	b	LBB2_1
LBB2_1:
	ldur	w8, [x29, #-8]
	subs	w8, w8, #2
	b.eq	LBB2_3
	b	LBB2_2
LBB2_2:
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [x8]
	adrp	x1, l_.str@PAGE
	add	x1, x1, l_.str@PAGEOFF
	bl	_fprintf
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB2_19
LBB2_3:
	ldur	w8, [x29, #-8]
	subs	w8, w8, #2
	b.ne	LBB2_7
	b	LBB2_4
LBB2_4:
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #8]
	adrp	x1, l_.str.1@PAGE
	add	x1, x1, l_.str.1@PAGEOFF
	bl	_strcmp
	cbz	w0, LBB2_6
	b	LBB2_5
LBB2_5:
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [x8]
	adrp	x1, l_.str.2@PAGE
	add	x1, x1, l_.str.2@PAGEOFF
	bl	_fprintf
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB2_19
LBB2_6:
	b	LBB2_7
LBB2_7:
	ldur	w8, [x29, #-8]
	subs	w8, w8, #5
	b.ne	LBB2_18
	b	LBB2_8
LBB2_8:
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #8]
	adrp	x1, l_.str.3@PAGE
	add	x1, x1, l_.str.3@PAGEOFF
	bl	_strcmp
	cbz	w0, LBB2_11
	b	LBB2_9
LBB2_9:
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #8]
	adrp	x1, l_.str.4@PAGE
	add	x1, x1, l_.str.4@PAGEOFF
	bl	_strcmp
	cbz	w0, LBB2_11
	b	LBB2_10
LBB2_10:
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [x8]
	adrp	x1, l_.str.5@PAGE
	add	x1, x1, l_.str.5@PAGEOFF
	bl	_fprintf
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB2_19
LBB2_11:
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #16]
	mov	x1, #0
	mov	w2, #10
	bl	_strtol
	stur	x0, [x29, #-24]
	ldur	x0, [x29, #-24]
	bl	_len
	str	w0, [sp, #12]                   ; 4-byte Folded Spill
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #16]
	bl	_strlen
	mov	x8, x0
	ldr	w0, [sp, #12]                   ; 4-byte Folded Reload
                                        ; kill: def $w8 killed $w8 killed $x8
	subs	w8, w0, w8
	b.eq	LBB2_13
	b	LBB2_12
LBB2_12:
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [x8]
	adrp	x1, l_.str.6@PAGE
	add	x1, x1, l_.str.6@PAGEOFF
	bl	_fprintf
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB2_19
LBB2_13:
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #24]
	adrp	x1, l_.str.7@PAGE
	add	x1, x1, l_.str.7@PAGEOFF
	bl	_fopen
	str	x0, [sp, #32]
	ldr	x8, [sp, #32]
	cbnz	x8, LBB2_15
	b	LBB2_14
LBB2_14:
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [x8]
	adrp	x1, l_.str.8@PAGE
	add	x1, x1, l_.str.8@PAGEOFF
	bl	_fprintf
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB2_19
LBB2_15:
	ldr	x0, [sp, #32]
	bl	_fclose
	ldur	x8, [x29, #-16]
	ldr	x0, [x8, #32]
	adrp	x1, l_.str.9@PAGE
	add	x1, x1, l_.str.9@PAGEOFF
	bl	_fopen
	str	x0, [sp, #24]
	ldr	x8, [sp, #24]
	cbnz	x8, LBB2_17
	b	LBB2_16
LBB2_16:
	ldr	x8, [sp, #16]                   ; 8-byte Folded Reload
	ldr	x0, [x8]
	adrp	x1, l_.str.8@PAGE
	add	x1, x1, l_.str.8@PAGEOFF
	bl	_fprintf
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB2_19
LBB2_17:
	ldr	x0, [sp, #24]
	bl	_fclose
	b	LBB2_18
LBB2_18:
	stur	wzr, [x29, #-4]
	b	LBB2_19
LBB2_19:
	ldur	w0, [x29, #-4]
	ldp	x29, x30, [sp, #64]             ; 16-byte Folded Reload
	add	sp, sp, #80
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_encode_and_decode              ; -- Begin function encode_and_decode
	.p2align	2
_encode_and_decode:                     ; @encode_and_decode
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-32]!           ; 16-byte Folded Spill
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16
	sub	sp, sp, #1072
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w27, -24
	.cfi_offset w28, -32
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	stur	x8, [x29, #-24]
	str	w0, [sp, #32]
	str	x1, [sp, #24]
	ldr	x8, [sp, #24]
	ldr	x0, [x8, #24]
	adrp	x1, l_.str.7@PAGE
	add	x1, x1, l_.str.7@PAGEOFF
	bl	_fopen
	str	x0, [sp, #16]
	ldr	x8, [sp, #24]
	ldr	x0, [x8, #32]
	adrp	x1, l_.str.9@PAGE
	add	x1, x1, l_.str.9@PAGEOFF
	bl	_fopen
	str	x0, [sp, #8]
	b	LBB3_1
LBB3_1:                                 ; =>This Inner Loop Header: Depth=1
	ldr	x2, [sp, #16]
	add	x0, sp, #38
	mov	w1, #1026
	bl	_fgets
	cbz	x0, LBB3_7
	b	LBB3_2
LBB3_2:                                 ;   in Loop: Header=BB3_1 Depth=1
	ldr	x8, [sp, #24]
	ldr	x0, [x8, #8]
	adrp	x1, l_.str.3@PAGE
	add	x1, x1, l_.str.3@PAGEOFF
	bl	_strcmp
	cbnz	w0, LBB3_4
	b	LBB3_3
LBB3_3:                                 ;   in Loop: Header=BB3_1 Depth=1
	ldr	w1, [sp, #32]
	add	x0, sp, #38
	bl	_encode
	b	LBB3_4
LBB3_4:                                 ;   in Loop: Header=BB3_1 Depth=1
	ldr	x8, [sp, #24]
	ldr	x0, [x8, #8]
	adrp	x1, l_.str.4@PAGE
	add	x1, x1, l_.str.4@PAGEOFF
	bl	_strcmp
	cbnz	w0, LBB3_6
	b	LBB3_5
LBB3_5:                                 ;   in Loop: Header=BB3_1 Depth=1
	ldr	w1, [sp, #32]
	add	x0, sp, #38
	bl	_decode
	b	LBB3_6
LBB3_6:                                 ;   in Loop: Header=BB3_1 Depth=1
	ldr	x0, [sp, #8]
	adrp	x1, l_.str.10@PAGE
	add	x1, x1, l_.str.10@PAGEOFF
	mov	x9, sp
	add	x8, sp, #38
	str	x8, [x9]
	bl	_fprintf
	b	LBB3_1
LBB3_7:
	ldr	x0, [sp, #16]
	bl	_fclose
	ldr	x0, [sp, #8]
	bl	_fclose
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	ldur	x9, [x29, #-24]
	subs	x8, x8, x9
	b.ne	LBB3_9
	b	LBB3_8
LBB3_8:
	add	sp, sp, #1072
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #32             ; 16-byte Folded Reload
	ret
LBB3_9:
	bl	___stack_chk_fail
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #48
	stp	x29, x30, [sp, #32]             ; 16-byte Folded Spill
	add	x29, sp, #32
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	wzr, [x29, #-4]
	stur	w0, [x29, #-8]
	str	x1, [sp, #16]
	ldur	w0, [x29, #-8]
	ldr	x1, [sp, #16]
	bl	_test_of_args
	cbz	w0, LBB4_2
	b	LBB4_1
LBB4_1:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB4_8
LBB4_2:
	ldr	x8, [sp, #16]
	ldr	x0, [x8, #8]
	adrp	x1, l_.str.1@PAGE
	add	x1, x1, l_.str.1@PAGEOFF
	bl	_strcmp
	cbnz	w0, LBB4_6
	b	LBB4_3
LBB4_3:
	bl	_test
	cbz	w0, LBB4_5
	b	LBB4_4
LBB4_4:
	mov	w8, #1
	stur	w8, [x29, #-4]
	b	LBB4_8
LBB4_5:
	b	LBB4_7
LBB4_6:
	ldr	x8, [sp, #16]
	ldr	x0, [x8, #16]
	mov	x1, #0
	mov	w2, #10
	bl	_strtol
	str	x0, [sp, #8]
	ldr	x8, [sp, #8]
                                        ; kill: def $w8 killed $w8 killed $x8
	str	w8, [sp, #4]
	ldr	w0, [sp, #4]
	ldr	x1, [sp, #16]
	bl	_encode_and_decode
	b	LBB4_7
LBB4_7:
	stur	wzr, [x29, #-4]
	b	LBB4_8
LBB4_8:
	ldur	w0, [x29, #-4]
	ldp	x29, x30, [sp, #32]             ; 16-byte Folded Reload
	add	sp, sp, #48
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"The program receives 1 or 4 arguments only.\n"

l_.str.1:                               ; @.str.1
	.asciz	"test"

l_.str.2:                               ; @.str.2
	.asciz	"Usage: cipher test\n"

l_.str.3:                               ; @.str.3
	.asciz	"encode"

l_.str.4:                               ; @.str.4
	.asciz	"decode"

l_.str.5:                               ; @.str.5
	.asciz	"The given command is invalid.\n"

l_.str.6:                               ; @.str.6
	.asciz	"The given shift value is invalid.\n"

l_.str.7:                               ; @.str.7
	.asciz	"r"

l_.str.8:                               ; @.str.8
	.asciz	"The given file is invalid.\n"

l_.str.9:                               ; @.str.9
	.asciz	"w"

l_.str.10:                              ; @.str.10
	.asciz	"%s"

.subsections_via_symbols
