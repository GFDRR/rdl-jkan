---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-of-tulehu-area-eastern-part-of-salahutu-district-maluku-tengah-regency-m
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-of-tulehu-area-eastern-part-of-salahutu-district-maluku-tengah-regency-m
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-tulehu-area-eastern-part-of-salahutu-district-maluku-tengah-regency-m
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-tulehu-area-eastern-part-of-salahutu-district-maluku-tengah-regency-m
dataset_id: rdls_hel-idn_unosat_damageassessmenttulehuare_20191004
description: 'UNOSAT code: EQ20191001IDN This map illustrates satellite based structure
  damage assessment in the Eastern part of Salahutu District, Indonesia that was affected
  by the 6.8 magnitude earthquake of the 26th of September 2019 with an epicenter
  located north of Kamarian in Kairatu District. UNITAR-UNOSAT has identified within
  the extent of this map 6 potentially damaged structures around Teluhu village in
  Salahutu District. Taking into account the pre-building footprints provided by Humanitarian
  OpenStreetMap we estimate to less than 1% the total number of structures potentially
  damaged. Taking into account the type of structural damage and the satellite based
  damage assessment analysis characteristics and limitations; it is possible that
  the damage is underestimated. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-tulehu-area-eastern-part-of-salahutu-district-maluku-tengah-regency-m]'
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
    description: Building footprints in Tulehu area, Eastern Salahutu District, identified
      from pre-event OpenStreetMap data
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
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
  description: UNOSAT analysts compared pre-event building footprints from Humanitarian
    OpenStreetMap with post-earthquake satellite imagery acquired after the 26 September
    2019 magnitude 6.8 earthquake to identify structural damage. Visual interpretation
    of satellite imagery changes identified 6 potentially damaged structures in Tulehu
    village, with confidence levels and validation flags recorded for each feature.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
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
- href: https://data.humdata.org/dataset/damage-assessment-of-tulehu-area-eastern-part-of-salahutu-district-maluku-tengah-regency-m
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct structural damage to buildings assessed via satellite imagery
      comparison in Tulehu village, with 6 potentially damaged structures identified
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
  description: Indonesia - Damage assessment of Tulehu area, Eastern part of Salahutu
    District, Maluku Tengah Regency, Maluku Province (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20191001IDN/EQ20191001IDN_gdb.zip
  format: Geodatabase
  id: resource_b0015b12
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20191001IDN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Indonesia - Damage assessment of Tulehu area, Eastern part of Salahutu
    District, Maluku Tengah Regency, Maluku Province (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20191001IDN/EQ20191001IDN_SHP.zip
  format: null
  id: resource_15aacdc2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20191001IDN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-idn_unosat_damageassessmenttulehuare_20191004
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-10-04'
temporal_resolution: null
title: Indonesia - Damage assessment of Tulehu area, Eastern part of Salahutu District,
  Maluku Tengah Regency, Maluku Province
version: null
vulnerability: null
---
