using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Data;
using System.Data.Entity;
using OnlineEventsManagementSystemMVC.Models;

namespace OnlineEventsManagementSystemMVC.Controllers
{
    public class HomeController : Controller
    {
        // GET: Home
        public ActionResult Index()
        {
            return View();
        }
        public ActionResult About()
        {
            return View();
        }

        public ActionResult Events()
        {
            return View();
        }

        public ActionResult Gallery()
        {
            return View();
        }

        public ActionResult Contact()
        {
            return View();
        }

        public ActionResult Registration()
        {
            return View();
        }

        public ActionResult Login()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Registartion(TblRegister r1)
        {
            using (EventsDataEntities db = new EventsDataEntities())
            {
                if (ModelState.IsValid)
                {
                    db.TblRegisters.Add(r1);
                    db.SaveChanges();
                    ViewBag.message("Registration Sucessfully");
                    ModelState.Clear();
                }
            }
            return View(r1);
        }
        [HttpPost]
        public ActionResult Login(TblRegister r1)
        {
            using (EventsDataEntities db = new EventsDataEntities())
            {
                if (ModelState.IsValid)
                {
                    var log = db.TblRegisters.Where(a => a.userName.Equals(r1.userName) && a.password.Equals(r1.password)).FirstOrDefault();
                    if (log != null)
                    {
                        return RedirectToAction("Contact");
                    }

                    ViewBag.message("Login Sucessfully");
                    ModelState.Clear();
                }
            }
            return View(r1);
        }

    }
}
    
