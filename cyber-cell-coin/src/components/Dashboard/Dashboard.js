import React from 'react';
var NewComponent = React.createClass({
    render: function() {
      return (
        <div>
          {'{'}% extends 'layout.html' %{'}'}
          {'{'}% block body %{'}'}
          <h1>Welcome back  {'{'}{'{'}session.get('name'){'}'}{'}'}</h1>
          {'{'}% include 'includes/_messages.html' %{'}'}
          <p />
          <p> Your current balance is | {'{'}{'{'} balance {'}'}{'}'} | CYC</p>
          <div className="card mb-3">
            <div className="card-header">
              <i className="fas fa-chart-area" />
              Price of CyberCell coin (CYC)</div>
            <div className="card-body">
              <canvas id="myAreaChart" width="100%" height={30} />
            </div>
            <div className="card-footer small text-muted">Updated today at {'{'}{'{'}ct{'}'}{'}'}</div>
          </div>
          {/* DataTables Example */}
          <div className="card mb-3">
            <div className="card-header">
              <i className="fas fa-table" />
              Blockchain History</div>
            <div className="card-body">
              <div className="table-responsive">
                {'{'}% for block in blockchain %{'}'}
                {'{'}% endfor %{'}'}
                <table className="table table-bordered" id="dataTable" width="100%" cellSpacing={0}>
                  <thead>
                    <tr>
                      <th>Index</th>
                      <th>Transaction</th>
                      <th>Hash</th>
                    </tr>
                  </thead>
                  <tfoot>
                    <tr>
                      <th>Index</th>
                      <th>Transaction</th>
                      <th>Hash</th>
                    </tr>
                  </tfoot>
                  <tbody><tr>
                      <td>{'{'}{'{'}block.number{'}'}{'}'}</td>
                      <td>{'{'}{'{'}block.data{'}'}{'}'}</td>
                      <td>{'{'}{'{'}block.hash(){'}'}{'}'}</td>
                    </tr></tbody>
                </table>
              </div>
            </div>
            <div className="card-footer small text-muted">Last update : today at {'{'}{'{'}ct{'}'}{'}'}</div>
          </div>
          {'{'}% endblock %{'}'}
        </div>
      );
    }
  });