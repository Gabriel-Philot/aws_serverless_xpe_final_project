# Introduction

## Motivation 🌎

The goal of this project was the final stage of my MBA (Cloud Data Engineering) which is a free applied project. However, I took the opportunity to apply something I was already doing at work, so in this project I had the chance to introduce various improvements/experiments and features that I believed would add value in that context, both from a technical and a business perspective. Therefore, I recreated a hypothetical scenario similar to the data situation and sought sources that fit into this created context.

## Objectives 📌

Based on the project requirements provided by the institution, we would follow a stage of creation and modeling of what we would do for our thesis. The solution was previously conceived with a design thinking bias to establish the objectives and solution that will be built.

Sharing a bit of the timeline of how it was done, basically, we had the following:

* Two weeks of using various artifacts and design thinking techniques to shape the solution and arrive at a backlog.

* Three two-week sprints of hands-on work.

* One week to finalize results and conclusions, and we will have another week to present the project, so here I am in the middle to do the documentation and practice my presentation.

From the design thinking process, a hypothetical scenario was created featuring a financial market company. While another financial market project might not seem very creative, it provided a valuable opportunity to delve into this area. Although the knowledge gained about the business side was limited, keeping up with daily news was a valuable step forward. The choice of the financial market was influenced by previous job experiences, which involved frequent micro ingestions of data from various types and sources for logistics purposes. This highlighted the similarity with the data needs in the financial sector, without the need to exhaustively chase down data.

With this information, a solution architecture was designed that:

* Can scale without issues, meaning no matter how many assets there are or how many ingestions, it won't impact performance or data availability.
* Flexible, following the first point, able to scale up/down resources, with the ability to ingest data from any type of source (API, Webscrap, legacy databases etc.).
* Centralized data provision for clients and analysts (internal stakeholders).
* Low entry cost.

In this context, a Serverless solution on AWS would fit, which was how I practically built everything for my project (at my previous job I basically did everything with AWS Lambda, S3, and very little Glue, so this choice was quite timely for me to improve).



