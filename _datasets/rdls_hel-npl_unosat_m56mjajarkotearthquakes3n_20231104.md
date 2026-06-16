---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/m-5-6m-jajarkot-earthquakes-nepal-of-3-november-2023
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/m-5-6m-jajarkot-earthquakes-nepal-of-3-november-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/m-5-6m-jajarkot-earthquakes-nepal-of-3-november-2023
dataset_id: rdls_hel-npl_unosat_m56mjajarkotearthquakes3n_20231104
description: 'UNOSAT code EQ00231104NPL, GDACS Id: 1398938 This application provides
  geospatial information on ongoing satellite based-assessment related with the 5.6
  magnitude earthquakes in Nepal of the 04th of November 2023. Important note: The
  boundaries and names shown, and the designations used on this map do not imply official
  endorsement or acceptance by the United Nations. The United Nations Satellite Centre
  -UNOSAT is not responsible for the misuse or misrepresentation of the map.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/m-5-6m-jajarkot-earthquakes-nepal-of-3-november-2023]'
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
    description: Population exposed to earthquake ground shaking in the affected area
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
  description: UNOSAT analysts reviewed and compared satellite imagery from before
    and after the 3-4 November 2023 earthquake to identify ground effects and assess
    population exposure. The resulting geospatial assessment quantifies affected population
    in the Jajarkot region using satellite-derived observations.
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
- href: https://data.humdata.org/dataset/m-5-6m-jajarkot-earthquakes-nepal-of-3-november-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by the 5.6 magnitude earthquake based on satellite
      assessment
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
        metric: exposure
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
  description: M 5.6M Jajarkot Earthquakes, Nepal of 3 November 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3721/UNOSAT_PopulationExposed_EQ20231104NPL_4Nov2023%20-%20Copy.xlsx
  format: null
  id: resource_8eeef317
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposed_EQ20231104NPL_4Nov2023 - Copy.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-npl_unosat_m56mjajarkotearthquakes3n_20231104
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-04'
temporal_resolution: null
title: M 5.6M Jajarkot Earthquakes, Nepal of 3 November 2023
version: null
vulnerability: null
---
