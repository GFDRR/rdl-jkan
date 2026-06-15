---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-
dataset_id: rdls_hel-bgd_unosat_floodimpactanalysischhata_20240701
description: "UNOSAT code: FL20240502BGD, GDACS ID: 1102700 This map illustrates satellite-detected\
  \ surface waters in Chhatak Upazila, Sunamganj District, Sylhet division, as observed\
  \ from a GLOBAL satellite image acquired on 26 June 2024 at 05:58 local time. Within\
  \ the analysed area, about 20 km\xC2\xB2 of land appears to be flooded. Furthermore,\
  \ within the analysed area, about 3,350 structures are identified as potentially\
  \ affected by the floods (30% of the total structures in the analysed area), along\
  \ with about 40 km of roads, as of 26 June 2024 This is a preliminary analysis and\
  \ has not yet been validated in the field. Please send ground feedback to the United\
  \ Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-]"
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
    description: Building structures in Chhatak Upazila identified as potentially
      affected by flood inundation
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
- asset_type:
    description: Road network segments in the analysed area potentially affected by
      flooding
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed satellite imagery acquired on 26 June 2024
    over Chhatak Upazila, comparing multi-temporal images to detect notable changes
    in surface water extent. Flooded areas were delineated, and spatial overlays with
    building footprints and road networks were performed to quantify potentially affected
    structures and infrastructure. This post-event empirical analysis provides rapid
    damage assessment for humanitarian response.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-impact-analysis-in-chhatak-upazila-sunamganj-district-sylhet-division-bangladesh-as-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Approximately 3,350 structures identified as potentially affected
      by floods (30% of total structures in analysed area)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Approximately 40 km of roads potentially affected by flood inundation
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact analysis in Chhatak Upazila, Sunamganj District, Sylhet
    Division, Bangladesh as of 26 June 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3889/TC20240502BGD_GDB.zip
  format: Geodatabase
  id: resource_c0dc723b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood impact analysis in Chhatak Upazila, Sunamganj District, Sylhet
    Division, Bangladesh as of 26 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3889/TC20240502BGD_SHP.zip
  format: null
  id: resource_ded83847
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgd_unosat_floodimpactanalysischhata_20240701
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-07-01'
temporal_resolution: null
title: Flood impact analysis in Chhatak Upazila, Sunamganj District, Sylhet Division,
  Bangladesh as of 26 June 2024
version: null
vulnerability: null
---
