---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-tropical-cyclone-yagi-population-exposure-analysis-in-viet-nam-07-september-2024
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-tropical-cyclone-yagi-population-exposure-analysis-in-viet-nam-07-september-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-tropical-cyclone-yagi-population-exposure-analysis-in-viet-nam-07-september-2024
dataset_id: rdls_hel-vnm_unosat_tropicalcycloneyagipopula_20240910
description: 'UNOSAT code: TC20240905VNM, GDACS ID: 1001090 Tropical Cyclone Yagi,
  the second-most powerful storm of 2024, caused widespread devastation across Southeast
  Asia. It formed in early September, making landfall in the Philippines before moving
  toward China and Vietnam. With wind speeds exceeding 245 km/h, Yagi caused severe
  damage, leading to widespread power outages, destruction of infrastructure, and
  loss of lives. Vietnam was particularly hard hit, with at least fourteen fatalities
  and many injured. The storm also disrupted transportation, forcing the cancellation
  of hundreds of flights and the closure of schools and public services. According
  to the information by GDACS, tropical cyclone YAGI can have a high humanitarian
  impact based on the maximum sustained wind speed, exposed population, and vulnerability.
  Approximately 23 million people, representing a significant portion of the total
  population, are living within areas where wind speeds exceed 120 km/h.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/unosat-tropical-cyclone-yagi-population-exposure-analysis-in-viet-nam-07-september-2024]'
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
    description: Population exposed to tropical cyclone Yagi in Vietnam
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
  - analysis_type: probabilistic
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery before and
    after Tropical Cyclone Yagi to identify population exposure and assess impacts.
    The analysis integrated observed wind field data from the cyclone event with spatial
    population data to quantify exposure and document direct losses including fatalities
    and infrastructure damage.
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
- href: https://data.humdata.org/dataset/unosat-tropical-cyclone-yagi-population-exposure-analysis-in-viet-nam-07-september-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Direct fatalities from Tropical Cyclone Yagi in Vietnam
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
        metric: death
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage including power outages and transportation
      disruption from Tropical Cyclone Yagi
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
  description: UNOSAT - Tropical Cyclone YAGI Population Exposure Analysis in Viet
    Nam - 07 September 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3958/UNOSAT_PopulationExposureAnalysis_TC_YAGI_VIETNAM_07SEP2024_0600UTC.xlsx
  format: null
  id: resource_0d3d88ba
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposureAnalysis_TC_YAGI_VIETNAM_07SEP2024_0600UTC.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vnm_unosat_tropicalcycloneyagipopula_20240910
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-09-10'
temporal_resolution: null
title: UNOSAT - Tropical Cyclone YAGI Population Exposure Analysis in Viet Nam - 07
  September 2024
version: null
vulnerability: null
---
