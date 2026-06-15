---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/m6-8-adassil-earthquake-sw-marrakesh-on-9-september-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/m6-8-adassil-earthquake-sw-marrakesh-on-9-september-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/m6-8-adassil-earthquake-sw-marrakesh-on-9-september-2023
dataset_id: rdls_hel-mar_unosat_m68adassilearthquakeswmar_20230909
description: 'UNOSAT code EQ20230909MAR, GDACS Id: 1390643 This application provides
  geospatial information on ongoing satellite based-assessment related with the 6.8
  magnitude earthquake in Morocco of the 08th of September 2023 (22:11 UTC) with a
  mainshock epicentre located 70 SW of Marrakesh city. Important note: The boundaries
  and names shown, and the designations used on this map do not imply official endorsement
  or acceptance by the United Nations. The United Nations Satellite Centre -UNOSAT
  is not responsible for the misuse or misrepresentation of the map.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/m6-8-adassil-earthquake-sw-marrakesh-on-9-september-2023]'
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
    description: Population exposed to earthquake ground shaking in the affected region
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
- asset_type:
    description: Building stock exposed to earthquake ground motion
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    earthquake:
    - analysis_type: probabilistic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: PGA:g
        process: ground_motion
        trigger: null
        type: earthquake
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts conducted post-event satellite imagery analysis comparing
    pre- and post-earthquake images to identify building damage and assess population
    exposure in the epicentral region 70 km southwest of Marrakesh. The resulting
    population exposure analysis integrates satellite-derived damage observations
    with spatial population data to quantify direct impacts from the M6.8 mainshock.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/m6-8-adassil-earthquake-sw-marrakesh-on-9-september-2023
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from M6.8 earthquake ground motion
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Morocco - M6.8 Adassil earthquake (SW Marrakesh) on 9 September 2023
    (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3663/UNOSAT_PopulationExposureAnalysis_EQ20230909MAR.xlsx
  format: null
  id: resource_b1ee9035
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_EQ20230909MAR.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mar_unosat_m68adassilearthquakeswmar_20230909
spatial:
  bbox: null
  centroid: null
  countries:
  - MAR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-09-09'
temporal_resolution: null
title: Morocco - M6.8 Adassil earthquake (SW Marrakesh) on 9 September 2023
version: null
vulnerability: null
---
