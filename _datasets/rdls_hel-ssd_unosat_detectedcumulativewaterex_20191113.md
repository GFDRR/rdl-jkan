---
attributions:
- entity:
    affiliation: null
    email: null
    name: VIIRS-NOAA satellite imagery
    url: https://data.humdata.org/dataset/cumulative-water-extents-as-of-06-november-2019-over-luakpiny-nasir-pibor
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population estimates
    url: https://data.humdata.org/dataset/cumulative-water-extents-as-of-06-november-2019-over-luakpiny-nasir-pibor
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-water-extents-as-of-06-november-2019-over-luakpiny-nasir-pibor
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-water-extents-as-of-06-november-2019-over-luakpiny-nasir-pibor
dataset_id: rdls_hel-ssd_unosat_detectedcumulativewaterex_20191113
description: 'UNOSAT code: FL20191023SSD This map illustrates the 5-day cumulative,
  day-time surface water extent detected over Luakpiny/Nasir, Pibor and neighbouring
  counties in South Sudan. The extent was derived from VIIRS-NOAA satellite imagery
  between 2 and 6 November 2019 and includes all pixels with 0-100% open water. In
  the two counties of interest, about 9% of the population in Luakpiny/Nasir and 7%
  in Pibor may be affected by taking into account WorldPop population estimates. This
  is a preliminary analysis that has not yet been validated in the field. Please send
  any fieldbased comments to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/cumulative-water-extents-as-of-06-november-2019-over-luakpiny-nasir-pibor]'
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
    description: WorldPop population estimates in Luakpiny/Nasir and Pibor counties
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed VIIRS-NOAA satellite imagery acquired between
    2-6 November 2019 over Luakpiny/Nasir and Pibor counties, detecting cumulative
    day-time surface water extent by identifying pixels with 0-100% open water. Population
    exposure was estimated by intersecting the water extent with WorldPop gridded
    population data to quantify potentially affected residents in each county.
  sources:
  - id: source_1
    license: null
    name: VIIRS-NOAA satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population estimates
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cumulative-water-extents-as-of-06-november-2019-over-luakpiny-nasir-pibor
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by satellite-detected water extent (9% in Luakpiny/Nasir,
      7% in Pibor)
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
        metric: exposure
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
  description: South Sudan - Satellite-detected cumulative water extents, as of 06
    November 2019 over Luakpiny/Nasir, Pibor (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/FL20191023SSD/FL20191023SSD_gdb.zip
  format: Geodatabase
  id: resource_336a54da
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191023SSD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: South Sudan - Satellite-detected cumulative water extents, as of 06
    November 2019 over Luakpiny/Nasir, Pibor (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/FL20191023SSD/FL20191023SSD_SHP.zip
  format: null
  id: resource_9a097559
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20191023SSD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ssd_unosat_detectedcumulativewaterex_20191113
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-11-13'
temporal_resolution: null
title: South Sudan - Satellite-detected cumulative water extents, as of 06 November
  2019 over Luakpiny/Nasir, Pibor
version: null
vulnerability: null
---
