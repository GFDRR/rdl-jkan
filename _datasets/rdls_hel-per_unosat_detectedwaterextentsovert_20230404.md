---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/water-extents-over-tumbes-and-zarumilla-districts-tumbes-province-peru-as-of-30-march-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extents-over-tumbes-and-zarumilla-districts-tumbes-province-peru-as-of-30-march-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-tumbes-and-zarumilla-districts-tumbes-province-peru-as-of-30-march-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-over-tumbes-and-zarumilla-districts-tumbes-province-peru-as-of-30-march-2023
dataset_id: rdls_hel-per_unosat_detectedwaterextentsovert_20230404
description: "UNOSAT code FL20230321PER, GDACS Id: 1365556 This map illustrates satellite-detected\
  \ water using Sentinel-2 acquired on 30 March 2023, 10:52 local time over Tumbes\
  \ and Zarumilla Districts, Tumbes Province, Peru. Within the cloud free analyzed\
  \ areas of about 900 km\xB2, a total of about 11 km\xB2 of lands appear to be affected\
  \ with flood waters. Based on Worldpop population data and the flood water extent,\
  \ ~2,400 people are potentially exposed or living close to flooded areas. This is\
  \ a preliminary analysis and has not yet been validated in the field. Please send\
  \ ground feedback to the United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-over-tumbes-and-zarumilla-districts-tumbes-province-peru-as-of-30-march-2023]"
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
    description: Population potentially exposed or living close to flooded areas based
      on WorldPop data
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
  description: "Sentinel-2 satellite imagery from 30 March 2023 was analyzed by UNOSAT\
    \ to detect water extents through visual interpretation and multi-temporal comparison.\
    \ Detected flood water polygons (~11 km\xB2) were intersected with WorldPop population\
    \ grids to estimate ~2,400 people potentially exposed to flooded areas in Tumbes\
    \ and Zarumilla Districts."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-over-tumbes-and-zarumilla-districts-tumbes-province-peru-as-of-30-march-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by flood water extent detected via satellite
      imagery
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
  description: Satellite detected water extents over Tumbes and Zarumilla Districts,
    Tumbes Province, Peru as of 30 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3557/FL20230321PER_gdb.zip
  format: Geodatabase
  id: resource_2dd817e7
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230321PER_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Tumbes and Zarumilla Districts,
    Tumbes Province, Peru as of 30 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3557/FL0230321PER_SHP.zip
  format: null
  id: resource_f88afb1d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL0230321PER_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents over Tumbes and Zarumilla Districts,
    Tumbes Province, Peru as of 30 March 2023 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3557/Satellite%20detected%20water%20extents%20over%20Tumbes%20Provinces%2C%20Peru%20%20as%20of%2030%20March%202023.csv
  format: null
  id: resource_7724ba35
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Satellite detected water extents over Tumbes Provinces, Peru as of 30 March
    2023.csv
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-per_unosat_detectedwaterextentsovert_20230404
spatial:
  bbox: null
  centroid: null
  countries:
  - PER
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-04-04'
temporal_resolution: null
title: Satellite detected water extents over Tumbes and Zarumilla Districts, Tumbes
  Province, Peru as of 30 March 2023
version: null
vulnerability: null
---
