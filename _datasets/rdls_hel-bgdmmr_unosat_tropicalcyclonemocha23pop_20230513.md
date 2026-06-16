---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-13
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GDACS (Global Disaster Alert and Coordination System)
    url: https://data.humdata.org/dataset/unosat-tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-13
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-13
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-13
dataset_id: rdls_hel-bgdmmr_unosat_tropicalcyclonemocha23pop_20230513
description: 'UNOSAT code TC20230510BGD, GDACS Id: 1000970 Tropical Cyclone MOCHA
  formed over the southern Bay of Bengal on 11 May 2023 and has since then continued
  to move towards western Myanmar and southern Bangladesh. On 13 May 2023 06:00 UTC,
  the centre of the cyclone was located over the sea close to Sittwe City (the capital
  of Rakhine State, western Myanmar, south-eastern Bangladesh), with maximum sustained
  winds of 231 km/h. According to the forecast by GDACS, tropical cyclone MOCHA can
  have a high humanitarian impact based on the maximum sustained wind speed, exposed
  population, and vulnerability.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-13]'
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
    description: Population exposed to tropical cyclone MOCHA in Bangladesh and Myanmar
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
    calculation_method: observed
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
  description: UNOSAT analysts reviewed satellite imagery and cyclone track data from
    GDACS to assess population exposure to tropical cyclone MOCHA. The analysis integrated
    observed wind field parameters (231 km/h maximum sustained winds) with gridded
    population data to quantify humanitarian impact in Bangladesh and Myanmar at the
    time of landfall on 13 May 2023.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: GDACS (Global Disaster Alert and Coordination System)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-tropical-cyclone-mocha-23-population-exposure-analysis-in-bangladesh-and-myanmar-13
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposure and humanitarian impact assessment from tropical
      cyclone MOCHA wind hazard
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
  description: UNOSAT - Tropical Cyclone MOCHA 23 - Population Exposure Analysis in
    Bangladesh and Myanmar -13 May 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3589/UNOSAT_PopulationExposureAnalysis_TCMOCHA_Myanmar_Bangladesh_13May2023%20(1).xlsx
  format: null
  id: resource_16bfcb56
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_TCMOCHA_Myanmar_Bangladesh_13May2023 (1).xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgdmmr_unosat_tropicalcyclonemocha23pop_20230513
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  - BGD
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-13'
temporal_resolution: null
title: UNOSAT - Tropical Cyclone MOCHA 23 - Population Exposure Analysis in Bangladesh
  and Myanmar -13 May 2023
version: null
vulnerability: null
---
