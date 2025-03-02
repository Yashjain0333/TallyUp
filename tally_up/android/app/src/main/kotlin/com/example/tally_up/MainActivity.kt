package com.example.tally_up

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Build
import android.provider.Telephony
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.BinaryMessenger
import io.flutter.plugin.common.EventChannel
import io.flutter.plugin.common.MethodChannel

class MainActivity: FlutterActivity() {

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        val smsReceiver = object:EventChannel.StreamHandler,BroadcastReceiver(){
            var eventSink: EventChannel.EventSink? = null
            
            override fun onListen(arguments: Any?, events: EventChannel.EventSink?) {
                eventSink = events
                println("SMS listener started")
            }

            override fun onCancel(arguments: Any?) {
                eventSink = null
                println("SMS listener cancelled")
            }

            override fun onReceive(context: Context?, intent: Intent?) {
                println("SMS received in native code")
                if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT){
                    for (sms in Telephony.Sms.Intents.getMessagesFromIntent(intent)) {
                        try {
                            val messageMap = mapOf(
                                "message" to sms.displayMessageBody,
                                "date" to System.currentTimeMillis().toString(),
                                "sender" to (sms.displayOriginatingAddress ?: "Unknown")
                            )
                            println("Debug - Message Map Type: ${messageMap.javaClass}")
                            println("Debug - Message Map Content: $messageMap")
                            eventSink?.success(messageMap.toMap())
                        } catch (e: Exception) {
                            println("Error sending message: ${e.message}")
                            e.printStackTrace()
                        }
                    }
                }
            }
        }
        registerReceiver(smsReceiver, IntentFilter("android.provider.Telephony.SMS_RECEIVED"))
        EventChannel(flutterEngine.dartExecutor.binaryMessenger,"com.example.tally_up/smsStream")
            .setStreamHandler(smsReceiver)
    }
}