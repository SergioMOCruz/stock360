package com.example.stock360.utils.configuration

import android.content.Context
import org.json.JSONObject

object AppConfig {
    lateinit var authServiceUrl: String
    lateinit var userServiceUrl: String
    lateinit var authServiceApiKey: String
    lateinit var userServiceApiKey: String

    var jwtToken: String? = null

    fun load(context: Context) {
        val inputStream = context.resources.openRawResource(
            context.resources.getIdentifier("appsettings", "raw", context.packageName)
        )
        val json = inputStream.bufferedReader().use { it.readText() }

        val obj = JSONObject(json)
        authServiceUrl = obj.getString("authServiceUrl")
        userServiceUrl = obj.getString("userServiceUrl")
        authServiceApiKey = obj.getString("authServiceApiKey")
        userServiceApiKey = obj.getString("userServiceApiKey")
    }
}
