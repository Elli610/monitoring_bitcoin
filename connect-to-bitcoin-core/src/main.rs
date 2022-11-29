extern crate bitcoincore_rpc;

use bitcoincore_rpc::{Auth, Client, RpcApi};

fn main() {

    let rpc = Client::new("http://localhost:8333",
                          Auth::UserPass("username".to_string(),
                                         "password".to_string())).unwrap();
    let best_block_hash = rpc.get_best_block_hash().unwrap();
    println!("best block hash: {}", best_block_hash);
}