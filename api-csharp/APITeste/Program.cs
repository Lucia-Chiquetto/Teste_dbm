using APITeste.Repositories;
using APITeste.Services;
using Microsoft.EntityFrameworkCore;
using Repositories;

var builder = WebApplication.CreateBuilder(args);

// Configurar a conex�o com o banco de dados
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");

builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(connectionString));

// Adicionar servi�os ao cont�iner
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Configura��o de Inje��o de Depend�ncia
builder.Services.AddScoped<IPessoaService, PessoaService>();
builder.Services.AddScoped<IPessoaRepository, PessoaRepository>();

var app = builder.Build();

// Configura��o do pipeline HTTP
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
