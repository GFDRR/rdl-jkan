---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/power-supply-assessment-following-the-adassil-al-haouz-earthquake-8-september-2023-m6-8-us
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/power-supply-assessment-following-the-adassil-al-haouz-earthquake-8-september-2023-m6-8-us
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/power-supply-assessment-following-the-adassil-al-haouz-earthquake-8-september-2023-m6-8-us
dataset_id: rdls_hl-mar_unosat_powersupplyassessmentfoll_20230918
description: 'UNOSAT code EQ20230909MAR, GDACS Id: 1390643 Status: Power outage observed.
  Further action(s): continue monitoring No significant power outage observed in Marrakech
  (70 km NE mainshock epicentre), Taroudant (150 km SW Marrakech) and Chichaoua (75
  km SW Marrakech). By 17 September, power supply in Tameslouht (20 km SW Marrakech)
  has recovered to the level observed before the earthquake of 08 September 2023.
  On 14 September, Southeast of Amizmiz likely to have power outage. By 17 September,
  power supply in Amizmiz (50 km SW Marrakech) was still in recovery phase but not
  yet at the before earthquake level. On 14 September, no evidences of power outage
  is observed in rural areas such as Ait Iaaza (60 km SW mainshock epicentre) and
  Sidi Zouine (60 km NE mainshock epicentre).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/power-supply-assessment-following-the-adassil-al-haouz-earthquake-8-september-2023-m6-8-us]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared high-resolution night-time light satellite
    imagery acquired before and after the 8 September 2023 earthquake to detect changes
    in power supply across settlements in the Al Haouz region. Visual interpretation
    of radiometric differences in night-time lights identified areas with power outages
    and tracked recovery progression through 17 September 2023.
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
- href: https://data.humdata.org/dataset/power-supply-assessment-following-the-adassil-al-haouz-earthquake-8-september-2023-m6-8-us
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct power supply disruption and recovery assessment following
      the earthquake using night-time light imagery
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
  description: Morocco - Power Supply Assessment Following the Adassil/Al Haouz Earthquake
    (8 September 2023, M6.8) using High-resolution Night-time Light Images - 18 September
    2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3674/EQ20230909MAR_gdb.zip
  format: Geodatabase
  id: resource_17ba09e7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Morocco - Power Supply Assessment Following the Adassil/Al Haouz Earthquake
    (8 September 2023, M6.8) using High-resolution Night-time Light Images - 18 September
    2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3674/EQ20230909MAR_SHP.zip
  format: null
  id: resource_70887b95
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20230909MAR_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mar_unosat_powersupplyassessmentfoll_20230918
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
  start: '2023-09-18'
temporal_resolution: null
title: Morocco - Power Supply Assessment Following the Adassil/Al Haouz Earthquake
  (8 September 2023, M6.8) using High-resolution Night-time Light Images - 18 September
  2023
version: null
vulnerability: null
---
