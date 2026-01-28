import { Controller, Get } from '@nestjs/common';
import { ApiOperation, ApiResponse } from '@nestjs/swagger';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('health')
  @ApiOperation({ summary: 'Health check' })
  @ApiResponse({ status: 200, description: 'Service is healthy' })
  health() {
    return { status: 'ok' };
  }

  @Get('hello')
  @ApiOperation({ summary: 'Hello endpoint' })
  @ApiResponse({ status: 200, description: 'Returns a greeting' })
  getHello() {
    return this.appService.getHello();
  }
}
