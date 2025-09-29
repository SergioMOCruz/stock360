package com.example.stock360.data.remote.user

import com.example.stock360.utils.configuration.AppConfig
import com.example.stock360.utils.network.AuthInterceptor
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object UserApiClient {
    private val BASE_URL: String get() = AppConfig.userServiceUrl

    private val client = OkHttpClient.Builder()
        .addInterceptor(
            AuthInterceptor(
                apiKeyProvider = { AppConfig.userServiceApiKey },
                tokenProvider = { AppConfig.jwtToken }
            )
        )
        .build()

    val apiService: UserApiService by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .client(client)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(UserApiService::class.java)
    }
}
