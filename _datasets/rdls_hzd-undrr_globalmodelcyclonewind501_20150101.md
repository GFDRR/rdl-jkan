---
attributions:
- entity:
    affiliation: null
    email: null
    name: IBTrACS database
    url: https://data.humdata.org/dataset/cyclone-wind-100-years-return-period
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/cyclone-wind-100-years-return-period
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/cyclone-wind-100-years-return-period
dataset_id: rdls_hzd-undrr_globalmodelcyclonewind501_20150101
description: 'The tropical cyclonic strong wind model use information from 2594 historical
  tropical cyclones, topography, terrain roughness, and bathymetry.. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cyclone-wind-100-years-return-period]'
details: This dataset was generated using other global datasets; it should not be
  used for local applications (such as land use planning). The main purpose of GAR
  2015 datasets is to broadly identify high risk areas at global level and for identification
  of areas where more detailed data should be collected. Some areas may be underestimated
  or overestimated. Given this analysis was conducted using global datasets, the resolution
  of which is not sufficient for in-situ planning, it should not be used for critical
  (like life saving) decisions. UNISDR and collaborators should in no case be liable
  for misuse or misinterpretation of the presented results. The designations employed
  and the presentation of material on the maps do not imply the expression of any
  opinion whatsoever on the part of UNISDR or the Secretariat of the United Nations
  concerning the legal status of any country, territory, city or area or of its authorities,
  or concerning the delimitation of its frontiers or boundaries.
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 5
    events:
    - calculation_method: simulated
      description: Probabilistic tropical cyclone wind hazard model with maximum sustained
        wind speeds at 5 return periods derived from 2594 historical cyclone tracks
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_strong_wind
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_50yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: Probabilistic tropical cyclone wind hazard model with maximum sustained
        wind speeds at 5 return periods derived from 2594 historical cyclone tracks
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_strong_wind
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_100yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: Probabilistic tropical cyclone wind hazard model with maximum sustained
        wind speeds at 5 return periods derived from 2594 historical cyclone tracks
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_strong_wind
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_250yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.004
          probability: null
          return_period: 250
    - calculation_method: simulated
      description: Probabilistic tropical cyclone wind hazard model with maximum sustained
        wind speeds at 5 return periods derived from 2594 historical cyclone tracks
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_strong_wind
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_500yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.002
          probability: null
          return_period: 500
    - calculation_method: simulated
      description: Probabilistic tropical cyclone wind hazard model with maximum sustained
        wind speeds at 5 return periods derived from 2594 historical cyclone tracks
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_strong_wind
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: event_1000yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.001
          probability: null
          return_period: 1000
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
  type: strong_wind
license: CC-BY-4.0
lineage:
  description: Historical tropical cyclone tracks from IBTrACS were processed with
    topography, terrain roughness, and bathymetry data to generate a probabilistic
    wind hazard model using GAR15 methodology. Maximum sustained wind speeds were
    modeled at 5 explicit return periods (50, 100, 250, 500, 1000 years) and distributed
    as global gridded raster datasets.
  sources:
  - id: source_1
    license: null
    name: IBTrACS database
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/cyclone-wind-100-years-return-period
  rel: source
loss: null
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
  description: Global model of cyclone wind 50, 100, 250, 500 and 1000 years return
    period (Zipped grid file of cyclone wind 100 years return period (1,539 kb))
  download_url: https://data.humdata.org/dataset/6366ac1f-6bed-42e9-b96e-22ef81008931/resource/202221dd-a79d-4ce5-93d7-f34f7514aeb2/download/viento-mundo-tr100-int1-g152.zip
  format: ARC/INFO Grid
  id: resource_202221dd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIENTO_MUNDO_TR100_INT1_g152.zip
- access_url: http://risk.preventionweb.net/capraviewer/main.jsp?tab=3
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global model of cyclone wind 50, 100, 250, 500 and 1000 years return
    period (Link to cyclone data on GAR Risk viewer)
  download_url: null
  format: null
  id: resource_ecfb188b
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Link to cyclone data on GAR Risk viewer
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global model of cyclone wind 50, 100, 250, 500 and 1000 years return
    period (Zipped grid file of cyclone wind 1000 years return period (1,337 kb))
  download_url: https://data.humdata.org/dataset/6366ac1f-6bed-42e9-b96e-22ef81008931/resource/2d09f2cd-0fc8-420a-ac70-2450c2f251a0/download/viento-mundo-tr1000-int1-g151.zip
  format: ARC/INFO Grid
  id: resource_2d09f2cd
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIENTO_MUNDO_TR1000_INT1_g151.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global model of cyclone wind 50, 100, 250, 500 and 1000 years return
    period (Zipped grid file of cyclone wind 250 years return period (1,349 kb))
  download_url: https://data.humdata.org/dataset/6366ac1f-6bed-42e9-b96e-22ef81008931/resource/a4dacb38-ef02-491b-b2ce-6589ee425a7c/download/viento-mundo-tr250-int1-g153.zip
  format: ARC/INFO Grid
  id: resource_a4dacb38
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIENTO_MUNDO_TR250_INT1_g153.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global model of cyclone wind 50, 100, 250, 500 and 1000 years return
    period (Zipped grid file of cyclone wind 500 years return period (1,539 kb))
  download_url: https://data.humdata.org/dataset/6366ac1f-6bed-42e9-b96e-22ef81008931/resource/f5beebdc-8544-4acd-9b4f-57184cff24f8/download/viento-mundo-tr500-int1-g154.zip
  format: ARC/INFO Grid
  id: resource_f5beebdc
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIENTO_MUNDO_TR500_INT1_g154.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Global model of cyclone wind 50, 100, 250, 500 and 1000 years return
    period (Zipped grid file of cyclone wind 50 years return period (1,368 kb))
  download_url: https://data.humdata.org/dataset/6366ac1f-6bed-42e9-b96e-22ef81008931/resource/a03e914f-6f41-4817-848f-4b11dbe44af8/download/viento-mundo-tr50-int1-g155.zip
  format: ARC/INFO Grid
  id: resource_a03e914f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VIENTO_MUNDO_TR50_INT1_g155.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-undrr_globalmodelcyclonewind501_20150101
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-01'
temporal_resolution: null
title: Global model of cyclone wind 50, 100, 250, 500 and 1000 years return period
version: null
vulnerability: null
---
