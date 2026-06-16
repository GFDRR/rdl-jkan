---
attributions:
- entity:
    affiliation: null
    email: null
    name: 4TU.Centre for Research Data
    url: https://data.4tu.nl/
  id: '1'
  role: resource_provider
- entity:
    affiliation: null
    email: null
    name: Tom Russell
    url: https://www.eci.ox.ac.uk/person/tom-russell
  id: '3'
  role: processor
- entity:
    affiliation: null
    email: null
    name: 4TU.Centre for Research Data
    url: https://data.4tu.nl/
  id: attribution_publisher_migrated_1767801294813
  role: publisher
- entity:
    affiliation: null
    email: nadia.bloemendaal@vu.nl
    name: Nadia Bloemendaal
    url: https://data.4tu.nl/authors/8a084c6a-3315-4ba7-9768-dd1ba1825dbc
  id: attribution_creator_migrated_1767801294813
  role: creator
- entity:
    affiliation: null
    email: nadia.bloemendaal@vu.nl
    name: Nadia Bloemendaal
    url: https://vu.nl/en/about-vu/research-institutes/ivm
  id: attribution_contact_point_migrated_1767801294813
  role: contact_point
- entity:
    affiliation: null
    email: info@deltares.nl
    name: Deltares
    url: https://www.deltares.nl/en
  id: attribution_1767801783793
  role: collaborator
catalog: null
contact_point:
  affiliation: null
  email: null
  name: 4TU.Centre for Research Data
  url: https://data.4tu.nl/
creator:
  affiliation: null
  email: null
  name: Tom Russell
  url: https://www.eci.ox.ac.uk/person/tom-russell
dataset_id: rdls_hzd-storm_globaltropicalcyclonewind
description: Datasets containing probabilistic analysis of tropical cyclone maximum
  wind speed (in m/s) at fixed return periods and return periods at fixed wind speeds
  for present climate (1980-2018) and climate change scenarios (1979-2014 baseline
  and 2015-2050 projections); gridded products are ~10 km per basin, and city/island
  tables summarize conditions within 100 km. Climate change datasets incorporate signals
  from four GCMs (CMCC-CM2-VHR4, CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM).
details: "Datasets were generated with the statistical STORM algorithm. Present climate\
  \ dataset uses IBTrACS historical tracks (1980-2018) with ERA5 monthly-mean environmental\
  \ conditions. Climate change datasets add signals from four GCMs (CMCC-CM2-VHR4,\
  \ CNRM-CM6-1-HR, EC-Earth3P-HR, HadGEM3-GC31-HM) to project future conditions. A\
  \ 2-D parametric wind model was applied to produce ~10 km fields, and return periods\
  \ (or wind speeds) were derived empirically with Weibull's plotting formula. Datasets\
  \ include, for each grid cell (or city/island entry), the mean, standard deviation,\
  \ and 5-95% confidence intervals across 1,000 realizations; basin IDs (EP, NA, NI,\
  \ SI, SP, WP) and fixed value sets for return periods (10-10,000 yr) and wind speeds\
  \ (20-75 m s\u207B\xB9 with additional threshold values) are provided."
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 28
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '10'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 10
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '20'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 20
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '30'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 30
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '40'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 40
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '50'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '60'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 60
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '70'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 70
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '80'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 80
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '90'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 90
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '100'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '200'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 200
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '300'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 300
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '400'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 400
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '500'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 500
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '600'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 600
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '700'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 700
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '800'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 800
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '900'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 900
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '1000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 1000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '2000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 2000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '3000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 3000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '4000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 4000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '5000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 5000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '6000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 6000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '7000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 7000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '8000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 8000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '9000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 9000
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_rht4Fpeu
        intensity_measure: sws_10m:m/s
        process: tropical_cyclone
        trigger: null
        type: strong_wind
      id: '10000'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 10000
    frequency_distribution: user_defined
    hazards:
    - classification: null
      id: hazard_rht4Fpeu
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: HST
    occurrence_range: 1/10 to 1/10000 years
    seasonality: uniform
license: CC0-1.0
lineage: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: STORM - Synthetic Tropical cyclOne geneRation Model
  url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff
publisher:
  affiliation: null
  email: null
  name: 4TU.Centre for Research Data
  url: https://data.4tu.nl/
purpose: To supply consistent, high-resolution tropical-cyclone wind hazard metrics
  for present climate and climate change scenarios that support risk assessment, engineering
  design, and adaptation planning using a common methodology (Weibull plotting) across
  basins and for selected cities and islands.
referenced_by:
- author_names:
  - Nadia Bloemendaal
  - Ivan D. Haigh
  - Hans de Moel
  - Sanne Muis
  - Reindert J. Haarsma
  - Jeroen C. J. H. Aerts
  date_published: '2020-02-06'
  doi: https://doi.org/10.1038/s41597-020-0381-2
  id: '1'
  name: Generation of a global synthetic tropical cyclone hazard dataset using STORM
  url: https://www.nature.com/articles/s41597-020-0381-2
- author_names:
  - Nadia Bloemendaal
  - Hans de Moel
  - Sanne Muis
  - Jeroen C. J. H. Aerts
  - Ivan D. Haigh
  date_published: '2020-11-10'
  doi: https://doi.org/10.1038/s41597-020-00720-x
  id: reference_SoyNkUM8
  name: Estimation of global tropical cyclone wind speed probabilities using the STORM
    dataset
  url: https://www.nature.com/articles/s41597-020-00720-x
resources:
- access_url: https://data.4tu.nl/datasets/0ea98bdd-5772-4da8-ae97-99735e891aff/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The GeoTIFFs provided in the original STORM datasets have been mosaicked
    into single files with global extent for each climate model/return period. STORM_FIXED_RETURN_PERIODS_{STORM_MODEL}_{STORM_RP}_YR_RP.tif
  download_url: null
  format: GeoTIFF
  id: HST
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal:
    central_year: null
    duration: null
    end: '2014'
    start: '1979'
  temporal_resolution: null
  title: Global tropical cyclone wind speed maps by return period (historical 1979-2014)
- access_url: https://data.4tu.nl/datasets/504c838e-2bd8-4d61-85a1-d495bdc560c3/4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The GeoTIFFs provided in the original STORM datasets have been mosaicked
    into single files with global extent for each climate model/return period. STORM_FIXED_RETURN_PERIODS_{STORM_MODEL}_{STORM_RP}_YR_RP.tif
  download_url: null
  format: GeoTIFF
  id: PRJ_MEDIAN
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 10000
  temporal:
    central_year: null
    duration: null
    end: '2050'
    start: '2015'
  temporal_resolution: null
  title: Global tropical cyclone wind speed maps by return period (median projections
    2015-2050)
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-storm_globaltropicalcyclonewind
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Global tropical cyclone (wind speed) hazard, historical and projections
version: '4'
vulnerability: null
---
