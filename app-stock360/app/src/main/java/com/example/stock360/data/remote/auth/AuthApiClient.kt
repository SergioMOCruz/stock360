package com.example.stock360.data.remote.auth

import com.example.stock360.utils.configuration.AppConfig
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object AuthApiClient {
    private val BASE_URL: String get() = AppConfig.authServiceUrl

    val apiService: AuthApiService by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(AuthApiService::class.java)
    }
}
