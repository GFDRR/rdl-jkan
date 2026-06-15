---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/burundi-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Burundi
  url: https://data.humdata.org/dataset/burundi-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA Burundi
  url: https://data.humdata.org/dataset/burundi-humanitarian-needs-overview
dataset_id: rdls_lss-bdi_ochabdi_apercudesbesoinshumanitai_2017
description: "Cet ensemble de donn\xE9es pr\xE9sente les besoins humanitaires les\
  \ plus urgents et le nombre estim\xE9 de personnes ayant besoin d'assistance au\
  \ Burundi.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/burundi-humanitarian-needs-overview]"
details: There will not be an updated HNO in 2024 as Burundi will not be an HRP country
  anymore.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian Needs Overview data compiled by OCHA Burundi from multiple
    humanitarian partners using JIAF (Joint Inter-Agency Analysis Framework) methodology
    to estimate people in need (PIN) and humanitarian targets across sectors (health,
    nutrition, shelter, education, protection) disaggregated by gender and age, with
    annual revisions from 2017-2023.
  sources:
  - id: source_1
    license: null
    name: OCHA Burundi
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/burundi-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need (PIN) estimates across humanitarian sectors in Burundi,
      including flood-affected populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People in need (PIN) estimates across humanitarian sectors in Burundi,
      including drought-affected populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: People in need (PIN) estimates across humanitarian sectors in Burundi,
      including earthquake-affected populations
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_3
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://reliefweb.int/attachments/c188fdb3-23f2-4671-b83d-af5e8426fe94/Burundi%20HRP.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: PIN and Target 2023 mid-year revision for the SAME, Nutrition, and
    Health sectors.
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/27515686-ab77-4f25-b176-00a4f59bdd05/download/pin_cible_revise_20230725-1.xlsx
  format: null
  id: resource_27515686
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Burundi_PIN_Target_mid-year revision_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (Burundi HNO 2023)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/9d396e61-e708-48ab-b51e-f50579fa169a/download/burundi-pin-et-cible-2023-par-groupe-de-population-sadd-et-province_22decembre2022-1.xlsx
  format: null
  id: resource_9d396e61
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2023
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (Burundi HNO 2022)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/4b6cb80c-47ce-48fc-9752-5a446fcffadc/download/burundi_hno2022_jiaf1_1.xlsx
  format: null
  id: resource_4b6cb80c
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2022
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (Burundi HNO 2021)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/cda1cbe0-84f5-458f-974b-ef779b95582c/download/copie-de-burundi-2021-hno_hrp_data_final.xlsx
  format: null
  id: resource_cda1cbe0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2021.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (Burundi HNO 2020)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/139df9e2-4103-4e2d-99f2-577149d30b2d/download/burundi-hno-2020.xlsx
  format: null
  id: resource_139df9e2
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (Burundi HNO 2019)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/b6521dfc-a765-485c-9233-8d8e61ef4a20/download/burundi-hno-2019.xlsx
  format: null
  id: resource_b6521dfc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2019
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (Burundi HNO 2018)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/daa2ed05-d796-4aa8-b7f0-a3a46080bc23/download/burundi-hno-2018.xlsx
  format: null
  id: resource_daa2ed05
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2018
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (Burundi HNO 2017)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/0fb21657-2ee4-486f-9097-9be9b6af6bbc/download/0_final-compilation-with-refugees.xlsx
  format: null
  id: resource_0fb21657
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BDI_HNO_2017
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Burundi: Aper\xE7u des Besoins Humanitaires (CSV)"
  download_url: https://data.humdata.org/dataset/818d6828-7ae6-4871-aee3-41d5170ad2dc/resource/032180ef-708a-4d18-902f-c348ffe9f654/download/burundu-pin.csv
  format: null
  id: resource_032180ef
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: burundu-pin.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bdi_ochabdi_apercudesbesoinshumanitai_2017
spatial:
  bbox: null
  centroid: null
  countries:
  - BDI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2017-01-01'
temporal_resolution: null
title: "Burundi: Aper\xE7u des Besoins Humanitaires"
version: null
vulnerability: null
---
