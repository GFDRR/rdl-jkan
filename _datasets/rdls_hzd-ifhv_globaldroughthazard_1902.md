---
attributions:
- entity:
    affiliation: null
    email: null
    name: Climatology and Climate Services Laboratory's Global SPEI Database
    url: https://data.humdata.org/dataset/global-drought-hazard
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Institute for International Law of Peace and Armed Conflict
  url: https://data.humdata.org/dataset/global-drought-hazard
creator:
  affiliation: null
  email: null
  name: Institute for International Law of Peace and Armed Conflict
  url: https://data.humdata.org/dataset/global-drought-hazard
dataset_id: rdls_hzd-ifhv_globaldroughthazard_1902
description: 'The Global Drought Hazard project is a collection of spatial raster
  datasets that provide access to statistical extreme value analyses of the Standardised
  Precipitation Evapotranspiration Index (6-month SPEI) to identify high risk areas
  on a global scale. The source data are monthly spatial raster datasets from the
  Climatology and Climate Services Laboratory''s Global SPEI Database for the period
  from January 1902 to December 2018. Each raster dataset has a spatial resolution
  of about 0.5 degrees, the values of which we converted into time series for each
  grid cell. These time series are used to model the number of months above selected
  SPEI thresholds (e.g. SPEI -1.5 or lower) for a range of return periods (e.g. 100
  years) via Poisson-Generalized Pareto Point Process models.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/global-drought-hazard]'
details: 'This project is based on analyses of other spatial datasets and should not
  be used for local or regional applications. Its purpose is to identify areas of
  high drought risk and highlight regions where more and more accurate research data
  should be. Due to the generalized statistical approach of the analysis, some areas
  may be under- or overestimated. Suggested citation: Weller, Daniel & Mann, Holger
  (2022): Global Drought Hazard. A global raster data set of extreme value analyses
  of the Standardized Precipitation Evapotranspiration Index via Poisson-Generalized
  Pareto Point Process modelling. Distributed by The Humanitarian Data Exchange: Institute
  for International Law of Peace and Armed Conflict.'
exposure: []
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 6
    events:
    - calculation_method: simulated
      description: Probabilistic drought hazard model based on 6-month Standardised
        Precipitation Evapotranspiration Index (SPEI) extreme value analysis at 6
        return periods globally
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_25yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.04
          probability: null
          return_period: 25
    - calculation_method: simulated
      description: Probabilistic drought hazard model based on 6-month Standardised
        Precipitation Evapotranspiration Index (SPEI) extreme value analysis at 6
        return periods globally
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_50yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.02
          probability: null
          return_period: 50
    - calculation_method: simulated
      description: Probabilistic drought hazard model based on 6-month Standardised
        Precipitation Evapotranspiration Index (SPEI) extreme value analysis at 6
        return periods globally
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_100yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.01
          probability: null
          return_period: 100
    - calculation_method: simulated
      description: Probabilistic drought hazard model based on 6-month Standardised
        Precipitation Evapotranspiration Index (SPEI) extreme value analysis at 6
        return periods globally
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_250yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.004
          probability: null
          return_period: 250
    - calculation_method: simulated
      description: Probabilistic drought hazard model based on 6-month Standardised
        Precipitation Evapotranspiration Index (SPEI) extreme value analysis at 6
        return periods globally
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_500yr
      occurrence:
        deterministic: null
        empirical: null
        probabilistic:
          event_rate: 0.002
          probability: null
          return_period: 500
    - calculation_method: simulated
      description: Probabilistic drought hazard model based on 6-month Standardised
        Precipitation Evapotranspiration Index (SPEI) extreme value analysis at 6
        return periods globally
      disaster_identifiers: []
      hazard:
        classification: null
        id: hazard_drought
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
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
      intensity_measure: SPI:-
      process: meteorological_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Monthly SPEI raster data from the Global SPEI Database (1902-2018)
    at 0.5 degree resolution were subjected to statistical extreme value analysis
    to derive probabilistic drought hazard estimates. The analysis identified SPEI
    thresholds (1.5, 2.0, 2.5, 3.0+) and computed their occurrence frequencies at
    six return periods (25, 50, 100, 250, 500, 1000 years) to map global drought risk
    areas.
  sources:
  - id: source_1
    license: null
    name: Climatology and Climate Services Laboratory's Global SPEI Database
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/global-drought-hazard
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://spei.csic.es/spei_database/#map_name=spei06
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -3.0 or lower for a return period of 1000 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/772e5350-4d9e-46e9-a5c6-6aafc955ab5b/download/global-drought-spei-3.0-return-period-1000-years.tif
  format: null
  id: resource_772e5350
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 3.0+ Return Period 1000 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -3.0 or lower for a return period of 500 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/b0b6422b-82e6-4bd3-8aea-e028611b87f7/download/global-drought-spei-3.0-return-period-500-years.tif
  format: null
  id: resource_b0b6422b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 3.0+ Return Period 500 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -3.0 or lower for a return period of 250 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/4487541d-84ef-4763-97a0-92a3c730514d/download/global-drought-spei-3.0-return-period-250-years.tif
  format: null
  id: resource_4487541d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 3.0+ Return Period 250 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -3.0 or lower for a return period of 100 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/e58ff655-72cb-4565-92af-4ceb3730c657/download/global-drought-spei-3.0-return-period-100-years.tif
  format: null
  id: resource_e58ff655
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 3.0+ Return Period 100 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -3.0 or lower for a return period of 50 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/97161fb1-3161-47d6-b4b6-fccf79461ba6/download/global-drought-spei-3.0-return-period-50-years.tif
  format: null
  id: resource_97161fb1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 3.0+ Return Period 50 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -3.0 or lower for a return period of 25 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/10b998e2-be41-483e-a662-52706937923c/download/global-drought-spei-3.0-return-period-25-years.tif
  format: null
  id: resource_10b998e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 3.0+ Return Period 25 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.5 or lower for a return period of 1000 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/b8655e91-ed6f-4304-8c48-ef3a54c77e05/download/global-drought-spei-2.5-return-period-1000-years.tif
  format: null
  id: resource_b8655e91
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.5+ Return Period 1000 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.5 or lower for a return period of 500 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/956544da-03ae-451a-a85a-7b976be0dd14/download/global-drought-spei-2.5-return-period-500-years.tif
  format: null
  id: resource_956544da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.5+ Return Period 500 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.5 or lower for a return period of 250 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/32e15d48-b03b-47b3-8fd2-6a110a9e0523/download/global-drought-spei-2.5-return-period-250-years.tif
  format: null
  id: resource_32e15d48
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.5+ Return Period 250 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.5 or lower for a return period of 100 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/2f4890c7-593a-4790-b7fb-ad8626718b43/download/global-drought-spei-2.5-return-period-100-years.tif
  format: null
  id: resource_2f4890c7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.5+ Return Period 100 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.5 or lower for a return period of 50 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/60e43ac3-31ba-4b89-91c3-6c293f4e7c49/download/global-drought-spei-2.5-return-period-50-years.tif
  format: null
  id: resource_60e43ac3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.5+ Return Period 50 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.5 or lower for a return period of 25 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/8e786a75-1c73-46df-8e62-4fdf6d52c633/download/global-drought-spei-2.5-return-period-25-years.tif
  format: null
  id: resource_8e786a75
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.5+ Return Period 25 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.0 or lower for a return period of 1000 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/8b617ce9-3ef2-44cd-a1f7-fd7397ec720d/download/global-drought-spei-2.0-return-period-1000-years.tif
  format: null
  id: resource_8b617ce9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.0+ Return Period 1000 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.0 or lower for a return period of 500 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/430b28bb-b255-453f-9426-60eb1ed1a087/download/global-drought-spei-2.0-return-period-500-years.tif
  format: null
  id: resource_430b28bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.0+ Return Period 500 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.0 or lower for a return period of 250 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/74fceaa8-e950-47ca-8bca-f1d8ef24fbdd/download/global-drought-spei-2.0-return-period-250-years.tif
  format: null
  id: resource_74fceaa8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.0+ Return Period 250 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.0 or lower for a return period of 100 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/e21f4f89-d2f6-484e-95d9-847679b44a61/download/global-drought-spei-2.0-return-period-100-years.tif
  format: null
  id: resource_e21f4f89
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.0+ Return Period 100 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.0 or lower for a return period of 50 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/08061f08-fed5-41f5-8234-7b9d94a7346b/download/global-drought-spei-2.0-return-period-50-years.tif
  format: null
  id: resource_08061f08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.0+ Return Period 50 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -2.0 or lower for a return period of 25 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/3d067bc4-e6bd-413e-a490-2010aa842a63/download/global-drought-spei-2.0-return-period-25-years.tif
  format: null
  id: resource_3d067bc4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 2.0+ Return Period 25 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.5 or lower for a return period of 1000 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/b8814be7-b176-4140-85aa-30fde540b9b6/download/global-drought-spei-1.5-return-period-1000-years.tif
  format: null
  id: resource_b8814be7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.5+ Return Period 1000 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.5 or lower for a return period of 500 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/eb934a71-ab3c-4e03-9b78-acf35abaa592/download/global-drought-spei-1.5-return-period-500-years.tif
  format: null
  id: resource_eb934a71
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.5+ Return Period 500 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.5 or lower for a return period of 250 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/add1394c-618d-41d9-a168-b1a8243d3dbc/download/global-drought-spei-1.5-return-period-250-years.tif
  format: null
  id: resource_add1394c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.5+ Return Period 250 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.5 or lower for a return period of 100 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/6744572e-d5d1-4033-9d64-c87dc565586a/download/global-drought-spei-1.5-return-period-100-years.tif
  format: null
  id: resource_6744572e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.5+ Return Period 100 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.5 or lower for a return period of 50 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/c5d8e7b5-de7e-435e-a2fb-9f9a36902b74/download/global-drought-spei-1.5-return-period-50-years.tif
  format: null
  id: resource_c5d8e7b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.5+ Return Period 50 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.5 or lower for a return period of 25 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/59b97435-f016-42b4-9546-57ce03d2ddcc/download/global-drought-spei-1.5-return-period-25-years.tif
  format: null
  id: resource_59b97435
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.5+ Return Period 25 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.0 or lower for a return period of 1000 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/1e3134d0-0b90-48d1-829a-f046cf8b6442/download/global-drought-spei-1.0-return-period-1000-years.tif
  format: null
  id: resource_1e3134d0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.0+ Return Period 1000 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.0 or lower for a return period of 500 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/0a6bd7da-5a45-437d-b311-29a60c0c675a/download/global-drought-spei-1.0-return-period-500-years.tif
  format: null
  id: resource_0a6bd7da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.0+ Return Period 500 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.0 or lower for a return period of 250 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/ee36b652-6d1f-47bc-afa6-37974c4c1a12/download/global-drought-spei-1.0-return-period-250-years.tif
  format: null
  id: resource_ee36b652
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.0+ Return Period 250 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.0 or lower for a return period of 100 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/0d5619c0-dbd4-4cd8-87e7-6a7082b8cac4/download/global-drought-spei-1.0-return-period-100-years.tif
  format: null
  id: resource_0d5619c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.0+ Return Period 100 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.0 or lower for a return period of 50 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/19a8be65-f87b-4567-8c29-ede5d4f2a24d/download/global-drought-spei-1.0-return-period-50-years.tif
  format: null
  id: resource_19a8be65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.0+ Return Period 50 Years.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: A spatial raster of the number of months with a Standardised Precipitation
    Evapotranspiration Index of -1.0 or lower for a return period of 25 years; data
    as of 30th September 2019; no planned updates - see metadata for more details
  download_url: https://data.humdata.org/dataset/30b85665-4c3d-4dc3-b543-3a567a3dea37/resource/38ee3c61-6130-4a26-b5b4-1106a477a689/download/global-drought-spei-1.0-return-period-25-years.tif
  format: null
  id: resource_38ee3c61
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Global Drought SPEI 1.0+ Return Period 25 Years.tif
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ifhv_globaldroughthazard_1902
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
  end: '2018-12-31'
  start: '1902-01-01'
temporal_resolution: null
title: Global Drought Hazard
version: null
vulnerability: null
---
