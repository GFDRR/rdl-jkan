---
attributions:
- entity:
    affiliation: null
    email: jrc-risk-data-hub@ec.europa.eu
    name: European Commision (EC), Joint Research Centre (JRC)
    url: https://joint-research-centre.ec.europa.eu/
  id: Entity_1
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: peter.salamon@ec.europa.eu
  name: Peter Salamon
  url: https://joint-research-centre.ec.europa.eu/
creator:
  affiliation: null
  email: jrc-risk-data-hub@ec.europa.eu
  name: European Commission, Joint Research Centre
  url: https://drmkc.jrc.ec.europa.eu/risk-data-hub#/
dataset_id: rdls_hzd-jrc_drmkc_riverflood
description: Probabilistic modelling of river flood hazard
details: 'River flood hazard maps for Europe and the Mediterranean Basin region is
  a gridded data set representing inundation along the river network, for nine different
  flood return periods (from 1-in-10-years to 1-in-500-years). The input river flow
  data for the new maps are produced by means of the open-source hydrological model
  LISFLOOD, while inundation simulations are performed with the hydrodynamic model
  LISFLOOD-FP. The extent comprises most of the geographical Europe and all the river
  basins entering the Mediterranean and Black Seas in the Caucasus, Middle East and
  Northern Africa countries. Flood hazard maps are generated for river basins > 150km2.
  Cell values indicate water depth (in m). The maps can be used to assess the exposure
  of population and economic assets to river floods, and to perform flood risk assessments.
  The dataset is created as part of the Copernicus Emergency Management Service. NOTE:
  this dataset is not an official flood hazard map (for details and limitations please
  refer to related publications).'
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 9
    events:
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: '75'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 75
    - calculation_method: simulated
      description: null
      disaster_identifiers: []
      hazard:
        classification: null
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
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
        id: JRC_River_Flood_Hazard
        intensity_measure: fl_wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: '500'
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: null
          probability: null
          return_period: 500
    frequency_distribution: null
    hazards:
    - classification: null
      id: JRC_River_Flood_Hazard
      intensity_measure: fl_wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: River_Flood_Hazard
    occurrence_range: 1/10 to 1/500 years
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type: null
    type: model
    url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c81
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Copernicus Emergency Management Service
  url: https://emergency.copernicus.eu/
publisher:
  affiliation: null
  email: jrc-risk-data-hub@ec.europa.eu
  name: European Commision (EC), Joint Research Centre (JRC)
  url: https://joint-research-centre.ec.europa.eu/
purpose: To assess the exposure of population and economic assets to river floods
  and support flood risk assessments in Europe and the Mediterranean Basin region.
referenced_by:
- author_names:
  - Calum Baugh
  - Juan Colonese
  - Claudia D'Angelo
  - Francesco Dottori
  - Jeffrey Neal
  - Christel Prudhomme
  - Peter Salamon
  date_published: '2024-03-08'
  doi: https://doi.org/10.2905/1D128B6C-A4EE-4858-9E34-6210707F3C81
  id: Ref_1
  name: River flood hazard maps for Europe and the Mediterranean Basin region
  url: http://data.europa.eu/89h/1d128b6c-a4ee-4858-9e34-6210707f3c81
resources:
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c81
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 10-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP10_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP10
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 10 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c82
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 20-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP20_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP20
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 20 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c83
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 30-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP30_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP30
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 30 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c84
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 40-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP40_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP40
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 40 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c85
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 50-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP50_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 50 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c86
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 75-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP75_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP75
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 75 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c87
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 100-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP100_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP100
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 100 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c88
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 200-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP200_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP200
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 200 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c89
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: 'Probabilistic river flood hazard maps (flood water depth in meter)
    for the 500-year return period, for Europe and the Mediterranean Basin region '
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_RP500_filled_depth.tif
  format: null
  id: River_Flood_Hazard_RP500
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: River Flood Hazard with 500 year Return Period
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c90
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: River flood hazard maps for Europe and the Mediterranean Basin region
    (The permanent water bodies used to patch the flood hazard maps)
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_permanent_water_bodies.tif
  format: null
  id: Permanent_Water_Bodies
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Permanent Water Bodies
- access_url: https://data.jrc.ec.europa.eu/dataset/1d128b6c-a4ee-4858-9e34-6210707f3c91
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: The spurious depth map that identifies areas where depths >10m are
    predicted in small channels (<3,000km^2) for the 10-year return period, plus a
    2km buffer.
  download_url: https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/CEMS-EFAS/flood_hazard/Europe_spurious_depth_areas.tif
  format: null
  id: Spurious_Depth_Areas
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 90
  temporal: null
  temporal_resolution: null
  title: Spurious Depth Areas
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-jrc_drmkc_riverflood
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  - description: Mediterranean Basin
    id: Location_2
    scheme: GEONAMES
    uri: https://www.geonames.org/12217088/mediterranean-basin.html
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: River flood hazard maps for Europe and the Mediterranean Basin region
version: '1'
vulnerability: null
---
