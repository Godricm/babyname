<template>
	<view>
		 <view class="padding bg-white">
			 <view class="text-left padding">
				 天格为根 - 天格乃祖先留下来的，为父母运势，其数理对个人影响不大。</br>
				 人格为苗 - 又称「主运」，是整个姓名的中心点，人一生的命运之好坏主要由此格推断。</br>
				 地格为花 - 又称为「前运」，主 38 岁以前，主管人中年以前的活动力。</br>
				 外格为叶 - 主管命运之灵力，一般指贵人或外来助力。为一个人外界和谐与否，可由此格看出。</br>
				 总格为果 - 主中年至晚年的命运，又称后运，主 38 岁以后。
			</view>
		</view>
		<form>
			<view class="cu-form-group">
				<view class="title">名字</view>
				<input placeholder="请输入你的名字" v-model="yourname" name="input"></input>
				<button :loading="btnLoading" class='cu-btn bg-green shadow' @click="findDestiny">查看</button>
			</view>
		</form>
		
		<view class="cu-list menu sm-border card-menu margin-top" v-if="status">
			<view class="cu-item">
				<view class="content">
					<text class="text-grey">姓名：{{status.name}}</text>
				</view>
			</view>
			<view class="cu-item">
				<view class="content">
					<text class="text-grey">天格：{{status.tian}}</text>
				</view>
			</view>
			<view class="cu-item">
				<view class="content">
					<text class="text-grey">人格：{{status.ren}}</text>
				</view>
			</view>
			<view class="cu-item">
				<view class="content">
					<text class="text-grey">地格：{{status.di}}</text>
				</view>
			</view>
			<view class="cu-item">
				<view class="content">
					<text class="text-grey">外格：{{status.wai}}</text>
				</view>
			</view>
			<view class="cu-item">
				<view class="content">
					<text class="text-grey">总格：{{status.zong}}</text>
				</view>
			</view>
			<view class="cu-item">
				<view class="content">
					<text class="text-grey">三才：{{status.sancai}}，{{status.sancai_type}}</text>
				</view>
			</view>
		</view>

	</view>
</template>

<script>
	import {
		wxLoginMixins
	} from '@/common/mixins/auth.js'
	import {
		searchDestiny
	} from '@/common/request/api/babyname/babyname.js'
	export default {
		data() {
			return {
				btnLoading: false,
				yourname: "",
				status: null,
			}
		},
		mixins: [wxLoginMixins],
		methods: {
			findDestiny() {
				this.btnLoading = true;
				this.status = null;
				searchDestiny(this.yourname).then(res => {
						this.status = res.data
					})
					.finally(() => {
						this.btnLoading = false
					});
			}
		}
	}
</script>

<style>
</style>