---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: hillaryhanselim7@gmail.com
  name: Hilary_Mvungi
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1549
creator:
  affiliation: null
  email: hillaryhanselim7@gmail.com
  name: Hilary_Mvungi
  url: https://crd.resilienceacademy.ac.tz/api/v2/users/1549
dataset_id: rdls_hzd-tza_resilienceacade_daressalaamerosionsuspect
description: "A GIS-based Erosion Susceptibility Model (ESM) was produced to support\
  \ the geomorphological assessment of the watercourses within Dar es Salaam, by JBA\
  \ Consulting. The ESM was developed to provide a transparent and replicable method\
  \ to generate a relative estimation of erosion susceptibility across the whole of\
  \ the study domain. ESM = Rainfall erosivity (used from The Global Rainfall Erosivity\
  \ Database (GloREDa) provided by the European Soil Data Centre (ESDAC)) \xD7 Soil\
  \ type (Calculated from the Dar es Salaam Sediment survey project produced by the\
  \ Ramani Huria Project and JBA Consulting under a World Bank project 'Dar es Salaam\
  \ Fluvial Geomorphology Assessment' (selection number 1256679)) \xD7 Built-up area\
  \ (calculated from The Global Human Settlement Layer (GHSL) on 2018) \xD7 (2\xD7\
  NDVI (calculated from Sentinel-2B sensor of the European Space Agency (ESA) collected\
  \ on 05/06/2018)) \xD7 Slope (calculated from the digital terrrain model (DTM) produced\
  \ by COWI ). *** Data download via Seafile cloud service. File options are for the\
  \ original file (larger) and compressed file (smaller).. [Source: This metadata\
  \ record was automatically extracted from the GeoNode portal resilienceacademy]"
details: Data fusion of datasets of different spatial resolutions. The fines resolution
  (5m) has been kept for the final product. WGS 1984 UTM Zone 37S.
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The model was produced with a particular aim in mind. It represents
    susceptibility of erosion at the time that the input datasets were collated. Importance
    needs to be given to the interpretation of the results. The quality of the model
    is dependent on the quality of the input datasets..
  sources:
  - id: source_1
    license: null
    name: Hilary_Mvungi
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://crd.resilienceacademy.ac.tz/catalogue/#/dataset/772
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Abal_25
  url: https://geonode.resilienceacademy.ac.tz
purpose: This dataset supports urban planning, climate risk assessment, and resilience
  building in Dar es Salaam.
referenced_by: []
resources:
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_erosion_suspectibility_model_compressed
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:32737
  description: 'Dar es Salaam Erosion Suspectibility Model_ 5m (OGC WMS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:dar_es_salaam_erosion_suspectibility_model_compressed&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geonode.resilienceacademy.ac.tz/datasets/geonode:geonode:dar_es_salaam_erosion_suspectibility_model_compressed
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:32737
  description: 'Dar es Salaam Erosion Suspectibility Model_ 5m (OGC WCS: geonode Service)'
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:dar_es_salaam_erosion_suspectibility_model_compressed
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32737
  description: Dar es Salaam Erosion Suspectibility Model_ 5m
  download_url: https://crd.resilienceacademy.ac.tz/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__dar_es_salaam_erosion_suspectibility_model_compressed&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:32737
  description: Dar es Salaam Erosion Suspectibility Model_ 5m
  download_url: https://crd.resilienceacademy.ac.tz/api/v2/assets/195/link
  format: null
  id: resource_3
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: dar_es_salaam_erosion_suspectibility_model_compressed
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tza_resilienceacade_daressalaamerosionsuspect
spatial:
  bbox:
  - 483860.0001
  - 9203730.0001
  - 560920.0001
  - 9280815.0001
  centroid: null
  countries:
  - TZA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2021
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Dar es Salaam Erosion Suspectibility Model_ 5m
version: null
vulnerability: null
---
