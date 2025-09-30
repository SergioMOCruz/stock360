package com.example.stock360.data.repository

import com.example.stock360.data.remote.auth.AuthApiClient
import com.example.stock360.domain.model.auth.LoginRequest
import com.example.stock360.utils.configuration.AppConfig

class AuthRepository {
    private val api = AuthApiClient.apiService

    suspend fun login(email: String, password: String): Boolean {
        val response = api.login(LoginRequest(email, password))
        return if (response.isSuccessful) {
            val token = response.body()?.accessToken
            AppConfig.jwtToken = token  // store JWT globally
            true
        } else {
            false
        }
    }
}
