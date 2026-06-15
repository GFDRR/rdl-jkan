---
attributions:
- entity:
    affiliation: null
    email: null
    name: NASA Precipitation Processing System (PPS)
    url: https://data.humdata.org/dataset/estimated-precipitation-accumulation-over-yemen-from-20th-july-to-1st-august-2021
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/estimated-precipitation-accumulation-over-yemen-from-20th-july-to-1st-august-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/estimated-precipitation-accumulation-over-yemen-from-20th-july-to-1st-august-2021
dataset_id: rdls_hzd-yem_unosat_estimatedprecipitationacc_20210806
description: 'UNOSAT code: FL20210729YEM This map illustrates the estimated total
  precipitation accumulated over Yemen. The total estimate was derived from the NASA
  Precipitation Processing System (PPS) dataset at a spatial resolution of approximately
  10km and covers the period from 20th July to 1st August 2021. Western Governorates
  have been predominantly affected by precipitation, with some values greater than
  600mm over the 13-day period. It is possible that precipitation levels may have
  been underestimated for local areas and are not a substitute for ground station
  measurements. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/estimated-precipitation-accumulation-over-yemen-from-20th-july-to-1st-august-2021]'
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
        process: pluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Precipitation accumulation data was derived from the NASA Precipitation
    Processing System satellite dataset at approximately 10km spatial resolution,
    covering the 13-day period from 20 July to 1 August 2021 over Yemen. UNOSAT analysts
    processed and mapped the satellite-derived precipitation estimates to identify
    areas of significant rainfall accumulation as a proxy for flood hazard potential.
  sources:
  - id: source_1
    license: null
    name: NASA Precipitation Processing System (PPS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/estimated-precipitation-accumulation-over-yemen-from-20th-july-to-1st-august-2021
  rel: source
loss:
  losses: []
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
  description: Estimated precipitation accumulation over Yemen from 20th July to 1st
    August 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/YE/FL20210729YEM/FL20210729YEM_gdb.zip
  format: Geodatabase
  id: resource_6e0547d5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729YEM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Estimated precipitation accumulation over Yemen from 20th July to 1st
    August 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/YE/FL20210729YEM/FL20210729YEM_shp.zip
  format: null
  id: resource_6f59ac2a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210729YEM_shp.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-yem_unosat_estimatedprecipitationacc_20210806
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-06'
temporal_resolution: null
title: Estimated precipitation accumulation over Yemen from 20th July to 1st August
  2021
version: null
vulnerability: null
---
