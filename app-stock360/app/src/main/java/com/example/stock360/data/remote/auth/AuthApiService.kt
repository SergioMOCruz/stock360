package com.example.stock360.data.remote.auth

import com.example.stock360.domain.model.auth.LoginRequest
import com.example.stock360.domain.model.auth.LoginResponse
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST

interface AuthApiService {
    @POST("auth/login")
    suspend fun login(@Body request: LoginRequest): Response<LoginResponse>
}
