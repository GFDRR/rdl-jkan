---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Resources Institute (WRI) Aqueduct Water Risk Atlas
    url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-baseline-water-stress
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-baseline-water-stress
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/icpac-geonode-ethiopia-baseline-water-stress
dataset_id: rdls_hzd-eth_icpac_baselinewaterstress_20250414
description: 'This dataset measures relative water demand. Higher values indicate
  more competition among users.The dataset has a resolution of 0.05 pixels about 5000
  metres ( referenced 2023) The baseline water stress (BWS) layer, developed as part
  of WRI''s Aqueduct Water Risk Atlas , measures the ratio of total water withdrawals
  relative to the annual available renewable surface water supplies. BWS serves as
  a good proxy for water-related challenges more broadly, given that areas of higher
  water stress will likely be subject to higher depletion of surface and groundwater
  resources and more competition amongst users, as well as the associated impacts
  on water quality and other ecosystem services. Watersheds with high baseline water
  stress may warrant greater need to take appropriate action to respond to watershed
  risks. A long time series of supply (1950&ndash;2010) was used to reduce the effect
  of multi-year climate cycles and ignore complexities of short-term water storage
  (e.g., dams, floodplains) for which global operational data are nonexistent. Baseline
  water stress thus measures chronic stress rather than drought stress. Watersheds
  with less than 0.012 m/m2 /year of withdrawal and 0.03 m/m2 /year of available blue
  water were masked as &ldquo;arid and low water use&rdquo; since watersheds with
  low values were more prone to error in the estimates of baseline water stress. Additionally,
  although current use in such catchments is low, any new withdrawals could easily
  push them into higher stress categories.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/icpac-geonode-ethiopia-baseline-water-stress]'
details: Time period is set to publication date rather than the date the data covers
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SMA:-
        process: hydrological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The baseline water stress layer was derived from WRI's Aqueduct Water
    Risk Atlas methodology, which calculates the ratio of total water withdrawals
    relative to annual available renewable surface water supplies. The resulting index
    was processed into a 0.05-degree resolution (approximately 5km) GeoTIFF raster
    for Ethiopia, with higher values indicating greater water competition and stress.
  sources:
  - id: source_1
    license: null
    name: World Resources Institute (WRI) Aqueduct Water Risk Atlas
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/icpac-geonode-ethiopia-baseline-water-stress
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
- access_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__eth_baseline_water_streass&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wfs
  coordinate_system: null
  description: GeoTIFF file. This dataset measures relative water demand. Higher values
    indicate more competition among users.The dataset has a resolution of 0.05 pixels
    about 5000 metres ( referenced 2023) The baseline water stress (BWS) layer, developed
    as part of WRI's Aqueduct Water Risk Atlas , measures the ratio of total water
    withdrawals relative to the annual available renewable surface water supplies.
    BWS serves as a good proxy for water-related challenges more broadly, given that
    areas of higher water stress will likely be subject to higher depletion of surface
    and groundwater resources and more competition amongst users, as well as the associated
    impacts on water quality and other ecosystem services. Watersheds with high baseline
    water stress may warrant greater need to take appropriate action to respond to
    watershed risks. A long time series of supply (1950&ndash;2010) was used to reduce
    the effect of multi-year climate cycles and ignore complexities of short-term
    water storage (e.g., dams, floodplains) for which global operational data are
    nonexistent. Baseline water stress thus measures chronic stress rather than drought
    stress. Watersheds with less than 0.012 m/m2 /year of withdrawal and 0.03 m/m2
    /year of available blue water were masked as &ldquo;arid and low water use&rdquo;
    since watersheds with low values were more prone to error in the estimates of
    baseline water stress. Additionally, although current use in such catchments is
    low, any new withdrawals could easily push them into higher stress categories.
  download_url: null
  format: null
  id: resource_1261555e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Ethiopia baseline water stress GeoTIFF
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-eth_icpac_baselinewaterstress_20250414
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-04-14'
temporal_resolution: null
title: Ethiopia baseline water stress
version: null
vulnerability: null
---
