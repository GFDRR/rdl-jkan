---
attributions:
- entity:
    affiliation: null
    email: null
    name: Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/unosat-tropical-cyclone-fiona-22-population-exposure-analysis-in-the-dominican-republic-20
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GDACS (Global Disaster Alert and Coordination System)
    url: https://data.humdata.org/dataset/unosat-tropical-cyclone-fiona-22-population-exposure-analysis-in-the-dominican-republic-20
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-tropical-cyclone-fiona-22-population-exposure-analysis-in-the-dominican-republic-20
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-tropical-cyclone-fiona-22-population-exposure-analysis-in-the-dominican-republic-20
dataset_id: rdls_hel-dom_unosat_tropicalcyclonefiona22pop_20220921
description: 'UNOSAT code TC20220920DOM, GDACS Id: 1000916 Tropical cyclone FIONA-22
  formed on 14 September 2022 over the Caribbean Sea east of Guadeloupe with the maximum
  sustained winds up to 220 km/h. The category 4 tropical cyclone FIONA-22 reached
  the coast of the Dominican Republic on 19 September 2022. According to GDACS, Tropical
  Cyclone FIONA-22 can have a high humanitarian impact based on the maximum sustained
  wind speed, exposed population, and vulnerability. Based on data of the forecasted
  tropical cyclone path of wind speeds zones from Joint Research Centre (Issued on
  20 September 2022 09:00 UTC), and population data from WorldPop Unconstrained 2020,
  UNITAR-UNOSAT has prepared a population exposure analysis for the Dominican Republic.
  About 66% of population of the Dominican Republic living inside wind speed zone
  below 60 km/h, 19% living inside wind speed zone of 60-120 km/h and 10% living inside
  wind speed zone above 120 km/h.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-tropical-cyclone-fiona-22-population-exposure-analysis-in-the-dominican-republic-20]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposed to tropical cyclone wind hazard zones in the Dominican
      Republic
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
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts integrated forecasted tropical cyclone wind speed zones
    from JRC with gridded population exposure data to assess population at risk from
    Tropical Cyclone Fiona-22 in the Dominican Republic. The analysis applied GDACS
    impact assessment methodology combining maximum sustained wind speeds, exposed
    population distribution, and vulnerability indicators to quantify humanitarian
    impact.
  sources:
  - id: source_1
    license: null
    name: Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: GDACS (Global Disaster Alert and Coordination System)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-tropical-cyclone-fiona-22-population-exposure-analysis-in-the-dominican-republic-20
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposure analysis to tropical cyclone Fiona-22 wind hazard
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: UNOSAT Tropical Cyclone Fiona-22, Population Exposure Analysis in the
    Dominican Republic - 20 September 2022 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3375/UNOSAT_Population_Exposure_FIONA22_DominicanRepublic_20September2022.xlsx
  format: null
  id: resource_39aa7b7d
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FIONA22_DominicanRepublic_20September2022.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-dom_unosat_tropicalcyclonefiona22pop_20220921
spatial:
  bbox: null
  centroid: null
  countries:
  - DOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-09-21'
temporal_resolution: null
title: UNOSAT Tropical Cyclone Fiona-22, Population Exposure Analysis in the Dominican
  Republic - 20 September 2022
version: null
vulnerability: null
---
