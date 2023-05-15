#include "boost/async.hpp"
#include "boost/async/main.hpp"
#include "boost/asio/steady_timer.hpp"

boost::async::main co_main(int argc, char * argv[]) 
{
  boost::asio::steady_timer tim{co_await boost::asio::this_coro::executor, std::chrono::milliseconds(500)}; 
  co_await tim.async_wait(boost::asio::deferred); 
  co_return 0; 
}
