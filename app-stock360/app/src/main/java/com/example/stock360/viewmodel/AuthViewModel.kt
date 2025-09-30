package com.example.stock360.viewmodel

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.stock360.data.remote.auth.AuthApiClient
import com.example.stock360.domain.model.auth.LoginRequest
import com.example.stock360.domain.model.auth.LoginResponse
import com.example.stock360.utils.types.Resource
import kotlinx.coroutines.launch

class AuthViewModel : ViewModel() {

    private val _loginState = MutableLiveData<Resource<LoginResponse>>()
    val loginState: LiveData<Resource<LoginResponse>> get() = _loginState

    fun login(email: String, password: String) {
        viewModelScope.launch {
            _loginState.value = Resource.Loading
            try {
                val request = LoginRequest(email = email, password = password)
                val response = AuthApiClient.apiService.login(request)

                if (response.isSuccessful) {
                    val body: LoginResponse? = response.body()
                    if (body != null) {
                        _loginState.value = Resource.Success(body)
                    } else {
                        _loginState.value = Resource.Error("Empty response")
                    }
                } else {
                    _loginState.value = Resource.Error(
                        "Error: ${response.code()} ${response.message()}"
                    )
                }
            } catch (e: Exception) {
                _loginState.value = Resource.Error("Exception: ${e.message}", e)
            }
        }
    }
}
