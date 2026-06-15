---
attributions:
- entity:
    affiliation: null
    email: null
    name: EC JRC INFORM team
    url: https://data.humdata.org/dataset/inform-subnational-risk-index-2021-south-east-europe
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UNDRR Regional Office for Europe and Central Asia (ROECA)
    url: https://data.humdata.org/dataset/inform-subnational-risk-index-2021-south-east-europe
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Secretariat of Disaster Preparedness and Prevention Initiative for South
      East Europe (DPPI SEE)
    url: https://data.humdata.org/dataset/inform-subnational-risk-index-2021-south-east-europe
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/inform-subnational-risk-index-2021-south-east-europe
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/inform-subnational-risk-index-2021-south-east-europe
dataset_id: rdls_el-albmkdmne_undrr_informsubnationalindex202_20211231
description: 'The INFORM subnational model for South East Europe for 3 pilot countries:
  Albania, Montenegro and North Macedonia, was initiated by UNDRR Regional Office
  for Europe and Central Asia (ROECA) and the Secretariat of Disaster Preparedness
  and Prevention Initiative for South East Europe (DPPI SEE) upon prior consent of
  all DPPI SEE Member States. The INFORM model has been developed under supervision
  of the EC''s JRC INFORM team and financial support from USAID BHA. The INFORM risk
  index results were produced in close collaboration with national and regional organization/data
  providers followed by regular meetings of the Regional Working Group (RWG) on INFORM.
  The RWG members are 2-3 representatives from each Government in the pilot countries
  (represented by their national civil protection authorities), including the Sendai
  Monitor National Focal Point, DPPI SEE Secretariat and UNDRR ROECA. Partners hope
  to use the model to improve cooperation between humanitarian and development actors
  in managing risk and building resilience across the region. INFORM identifies areas
  at a high risk of humanitarian crisis that are more likely to require international
  assistance. The INFORM model is based on risk concepts published in scientific literature
  and envisages three dimensions of risk: Hazards & Exposure, Vulnerability and Lack
  of Coping Capacity. The INFORM model is split into different levels to provide a
  quick overview of the underlying factors leading to humanitarian risk. The INFORM
  subnational model for South East Europe is developed at the first administrative
  level (corresponding to the subnational regions, capitals and municipalities) of
  Albania, Montenegro and North Macedonia. The INFORM risk index was calculated for
  44 administrative units. The INFORM index supports a proactive disaster risk management
  framework. It will be helpful for an objective allocation of resources for disaster
  risk reduction and management as well as for coordinated actions focused on anticipating,
  mitigating, and preparing for humanitarian emergencies. It also identifies areas
  for improvement in national disaster data availability and compliance with implementation
  of Sendai Framework for DRR, SDGs and other global initiatives.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/inform-subnational-risk-index-2021-south-east-europe]'
details: null
exposure:
- asset_type:
    description: Population exposed to multiple hazards in subnational administrative
      units
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The INFORM subnational risk index integrates multi-hazard exposure
    data, socioeconomic vulnerability indicators, and coping capacity assessments
    for three South East European countries (Albania, Montenegro, North Macedonia)
    using the EC JRC INFORM methodology. Data was compiled from national and regional
    organizations under UNDRR and DPPI SEE coordination to produce composite risk
    scores at subnational administrative levels.
  sources:
  - id: source_1
    license: null
    name: EC JRC INFORM team
    risk_data_type:
    - loss
    type: model
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: UNDRR Regional Office for Europe and Central Asia (ROECA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: Secretariat of Disaster Preparedness and Prevention Initiative for South
      East Europe (DPPI SEE)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/inform-subnational-risk-index-2021-south-east-europe
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population at risk from flood hazards in subnational risk assessment
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
    description: Population at risk from earthquake hazards in subnational risk assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
    description: Population at risk from strong wind hazards in subnational risk assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
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
  url: https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Risk/Methodology
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://drmkc.jrc.ec.europa.eu/inform-index/INFORM-Subnational-Risk/Subnational-Training
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 3 page infographic presenting main findings of INFORM subnational risk
    index 2021 results for South East Europe.
  download_url: https://data.humdata.org/dataset/42e31688-129f-4618-94f3-d786acd64730/resource/7b188baf-afdf-4ee7-8dce-a8c4efc991bf/download/inform-see2021_infographic_v0.1_10112021.pdf
  format: null
  id: resource_7b188baf
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM SEE2021_infographic_v0.1_10112021.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of North Macedonia, Albania, Montenegro - INFORM subnational
    risk index 2021, South East Europe (The INFORM subnational risk index results
    for 2021, South East Europe.)
  download_url: https://data.humdata.org/dataset/42e31688-129f-4618-94f3-d786acd64730/resource/83795509-ba2a-4ff7-9cbb-852d3e9fad25/download/inform_see_2021_v0.1_10112021.xlsx
  format: null
  id: resource_83795509
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: INFORM_SEE_2021_v0.1_10112021.xlsx
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-albmkdmne_undrr_informsubnationalindex202_20211231
spatial:
  bbox: null
  centroid: null
  countries:
  - MKD
  - ALB
  - MNE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-12-31'
temporal_resolution: null
title: Republic of North Macedonia, Albania, Montenegro - INFORM subnational risk
  index 2021, South East Europe
version: null
vulnerability: null
---
