package com.example.stock360.data.repository

import com.example.stock360.data.remote.user.UserApiClient

class UserRepository {
    private val api = UserApiClient.apiService

    suspend fun getUsers() = api.getUsers()
}
