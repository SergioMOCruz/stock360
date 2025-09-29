package com.example.stock360.utils.network

import okhttp3.Interceptor
import okhttp3.Response
import com.example.stock360.utils.configuration.AppConfig

class AuthInterceptor(
    private val apiKeyProvider: () -> String,
    private val tokenProvider: () -> String?
) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val requestBuilder = chain.request().newBuilder()

        // Always add API key (per service)
        requestBuilder.addHeader("x-api-key", apiKeyProvider())

        // Add JWT token if available
        tokenProvider()?.let { token ->
            requestBuilder.addHeader("Authorization", "Bearer $token")
        }

        return chain.proceed(requestBuilder.build())
    }
}
