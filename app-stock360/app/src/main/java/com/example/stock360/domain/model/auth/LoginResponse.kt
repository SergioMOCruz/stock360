package com.example.stock360.domain.model.auth

data class LoginResponse(
    val accessToken: String,
    val userId: String,
    val expiresIn: Long
)
