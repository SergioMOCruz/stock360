package com.example.stock360.data.remote.user

import com.example.stock360.domain.model.user.User
import retrofit2.Response
import retrofit2.http.GET
import retrofit2.http.Path

interface UserApiService {
    @GET("users/")
    suspend fun getUsers(): Response<List<User>>
}
